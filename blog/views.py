from django.shortcuts import render

def my_blog(request):
    return render(request, 'index.html')

