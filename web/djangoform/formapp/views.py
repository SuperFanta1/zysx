from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, template_name='index.html')


def sum(request):
    # <form>标签发送GET请求中?拼接的参数，称为Query String(查询字符串)
    # <form>标签POST请求中，参数放在请求体中，称为Form Data(表单数据)
    # <form>标签也成为表单。

    # 在这个函数中，要获取form标签发送的请求中，提交的input中输入的数据。
    if request.method == 'GET':
        # p1和p2是<input>标签中的name属性的值，并且必须是name属性的值。
        num1 = request.GET.get('p1', '0')
        num2 = request.GET.get('p2', '0')
        return HttpResponse(str(int(num1) + int(num2)))
    elif request.method == 'POST':
        num1 = request.POST.get('p1', '0')
        num2 = request.POST.get('p2', '0')
        return HttpResponse(str(int(num1) + int(num2)))

"""
1. <form>标签发送POST请求，必须携带{% csrf_token %}，这个csrf_token在浏览器上刷新页面的时候，会加载成一个标签<input type='hidden' name='csrfmiddlewaretoken' value='BciUrUDvqA2Fwl1lcxrgCCcxrZd6lZhSVAxba9zuBSIhHQQ4YkQ7Ur8HPj34GJLm' />，并且value的值每次刷新都是不一样的；
2. 如果POST请求不携带{% csrf_token %}，Django后台会拒绝浏览器的请求，不会执行相应的视图函数；出现403错误。
3. form标签提交POST请求的时候，会将用户输入的input数据以及这个隐藏的input数据放在请求体中，传给django后台；
"""

"""
csrf：是黑客攻击后台服务的一种常见方式。
"""

# Django数据库操作
from .models import People
def add_data(request):
    # 使用ORM进行数据的添加
    # 第一种添加数据的方式：
    # People.objects.create(p_name='张三', p_age=20)

    # 第二种添加数据方式：
    # p = People(p_name='李四', p_age=25)
    # p.save()

    # 查询所有数据，得到查询结果集：QuerySet类型的对象
    all_people = People.objects.all()
    print(all_people)
    for people in all_people:
        print(people.p_age, people.p_name)

    # 查询一个数据
    people = People.objects.get(p_name='李四')
    print(people.p_name, people.p_age)

    people = People.objects.get(id=1)
    print(people.p_name, people.p_age)

    # id=1且p_name='张三'的数据
    people = People.objects.get(id=1, p_name='王五')
    print(people.p_name, people.p_age)

    # 修改数据：先获取这个对象，然后再修改属性即可。
    obj = People.objects.get(id=1)
    obj.p_name = '王五'
    obj.p_age = 100
    obj.save()

    # 删除数据: 先获取这个对象，然后再删除即可。
    p = People.objects.get(p_name='李四')
    p.delete()

    return HttpResponse('数据添加成功')

