from django.shortcuts import render

# 前后端混合开发：前端工程师(30%=html页面) 后端工程师(70%=提供数据+渲染数据+处理数据)
# 前后端分离开发(djangorestframework框架)：前端工程师(70%=html页面+渲染数据+处理数据) 后端工程师(30%=提供json数据)

# 渲染模板：模板指的就是.html文件，渲染指的是将后台提供的数据展示到html的标签中。所以需要学习Django模板语法：{{  }}、{%  %}

# 模板文件中，如果要使用.css/.js等这些文件，应该如何引用。
# 1. 在项目根目录下新建一个文件夹，必须命名为 "static";
# 2. 将所有的静态资源文件(css、js、图片、音频等资源)，放到这个 static 文件夹中；
# 3. 在settings.py文件中配置：STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


class People(object):
    def __init__(self):
        self.name = '李四'
        self.age = 100

    def show_info(self):
        return '这个人的信息是：{}-{}'.format(self.name, self.age)

# time模块是Python内置的用于操作时间(秒)模块
# datetime模块是Python内置的用于操作日期(年月日时分秒)的模块
import time, datetime
def index(request):

    p = People()

    context = {
        'name': '张三',
        'book_list': ['Python', 'Java', 'C', 'C++'],
        'info': {
            'a': 10,
            'b': 20
        },
        # 从datetime.py这个模块中引入class datetime这个类，再调用类中的now()函数，从而获取当前日期和时间。
        'now_time': datetime.datetime.now(),
        'user': p
    }

    return render(request, template_name='index.html', context=context)
