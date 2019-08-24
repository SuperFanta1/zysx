from django.urls import path, include, re_path
# .表示当前目录；.views表示从当前目录下的views.py文件中import相关内容
from .views import index, index1, index3, index4

# url：路由
urlpatterns = [
    # 访问地址：入口路由+app下的子路由
    path('a/', index1),
    # url地址如何接收GET请求携带的参数：
    # GET：参数是放在url中的；?user=xxx&pwd=xxx
    # POST：该请求的参数是放在请求体中的，跟url地址没有关联的；
    path('pramas/', index),

    # GET请求参数通过路径的形式，传递给视图函数
    # 123和456就是要传递的参数
    # http://127.0.0.1:8000/blog/pramas/123/456/
    # <>表示要匹配的参数，int表示参数的类型
    path('path/<int:num1>/<str:num2>/', index3),

    # Django2.0版本之前，使用url()设置路由。
    # url(r'^test/$', index)
    # 正则表达式写法：^表示以re_test字符开头；$表示以re_test字符结尾；
    re_path(r'^re_test/$', index),

    # 正则表达式如何使用路径传参？
    # ()表示要提取的参数。\d+表示多位数的数字，不能写英文字母。\w+表示匹配多个英文字符或多个数字。
    re_path(r'^re_params/(\d+)/(\w+)/$', index4),

    # 正则表达式路径传参的第二种写法：
    # 关键字参数，django调用index4函数的时候，会这样调：index4(a=10, b=20)
    # (?P<a>\d+): 正则表达式提取\d+的内容，并且将这个内容赋值给形参a。
    re_path(r'^second/(?P<a>\d+)/(?P<b>\w+)/$', index4),
]
# def num(a, b):
#     pass
# 关键字参数
# num(a=10, b=20)

