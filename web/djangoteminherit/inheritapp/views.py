from django.shortcuts import render

"""
模板继承：
1. 可以将多个页面中可以共用的html代码，单独封装到一个html中，那么这多个页面可以通过继承这个公共的html，实现内容的加载；
2. 可以优化各个html页面，减少重复代码的出现次数，让html代码更加简洁；
"""

def index1(request):
    return render(request, template_name='index1.html')

def index2(request):
    return render(request, template_name='index2.html')
