from django.shortcuts import render, HttpResponse

# Django项目和app应用之间的关系：
# 一个Django项目可以管理多个app应用，其中，一个app应用对应着后台项目中的某一个模块。
# 一个项目可以划分为多个模块：比如用户模块(登录注册、用户名的检测、密码的找回等功能)，那么就可以给用户模块新建一个app应用叫userapp，所有的功能都可以写在这个userapp中。商品模块(首页商品、列表页商品、详情页商品、热门商品、商品搜索等功能)，此时再新建一个app应用叫goodsapp，所有关于商品的功能都可以写在这个goodsapp中。

# 为什么要创建多个app应用：
# 1. 让项目的结构更加清晰，后期维护起来比较方便。
# 2. 方便代码的编写，多人协作开发更方便快捷。

# views.py文件的作用：该文件主要就是处理Django接收过来的Request请求，然后返回Response响应。
def index(request):
    """
    视图函数：接收request请求对象，并返回response响应对象。
    :param request: 必须设置的参数。它用于接收Django后台框架传递过来的Request对象(前端)。
    :return:
    """
    if request.method == 'GET':
        res = request.GET.get('username', 'None') + request.GET.get('pwd', 'None')
        return HttpResponse(res)


def index3(request, num1, num2):
    # 形参num1和num2必须和path()路由中定义的参数名保持一致。
    print(type(num1), type(num2))
    return HttpResponse('a')


def index1(request):
    return HttpResponse('成功')


def index4(request, a, b):
    # 形参可以自定义任意字符，因为re_path()这个路由中没有指定参数名。这里的a和b都是字符串。
    res = a + '; ' + b
    return HttpResponse(res)

