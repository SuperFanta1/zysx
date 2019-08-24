"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 从app这个包中找到views.py文件，从这个文件中导入index函数
from app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # 新增了一个url地址 test/，这个地址就是用在浏览器中的，发送Request请求的。
    # 访问这个地址，想得到什么样的Response响应？
    # test/这个url地址，和index函数做了绑定，当前端浏览器访问test/地址的时候，Django框架就会自动调用index函数，并且Django框架会给index函数传递浏览器发送的Request对象。
    path('test/', index),
    # 将app这个应用下的urls，在url总入口文件中进行导入，所有的url都要经过这个总入口。
    path('blog/', include('app.urls'))
]
