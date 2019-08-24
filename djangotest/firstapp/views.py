from django.shortcuts import render, HttpResponse

# Create your views here.

# 这个文件就是来处理前端发送的GET/POST请求的。

#python manage.py startapp firstapp： 创建一个app应用，名称是firstapp。这里之所以称为app，是因为Django这个框架将一个项目分割成很多app应用，每一个app应用对应了项目中的一个模块。将项目中的每一个模块单独定义一个app，可以使项目的多人协作开发更加方便，结构更加清晰。

# 项目模块的划分：
# 用户模块：登陆注册、个人信息、密码找回、邮箱激活用户。
# 商品模块：首页、列表页、搜索、排序。
# 购物车和订单：

# 视图函数。
def index(request):
    if request.method == 'GET':
        return HttpResponse('Hello World!')
