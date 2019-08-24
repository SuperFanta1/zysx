"""djangotest URL Configuration

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
from django.urls import path
# from firstapp.views import index
# path('myfirst/', index),

from firstapp import views
# path('myfirst/', views.index),

urlpatterns = [
    path('admin/', admin.site.urls),
    # 给这个url地址，绑定对应的视图函数。当通过浏览器请求这个url地址的时候，django会自动调用index这个函数。
    # 以后注意：一个url对应一个视图函数，django会接收到前端的GET请求，并将这个请求交给index这个函数处理这个请求。将index返回的结果(Response)再返回给前端浏览器。
    path('myfirst/', views.index),
]
