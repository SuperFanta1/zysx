from django.shortcuts import render

def list(request):
    return render(request, template_name='list.html')

def add(request):
    return render(request, template_name='add.html')

def update(request):
    return render(request, template_name='update.html')
