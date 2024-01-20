# blog/views.py

from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post

def my_blog(request):
    return render(request, 'index.html')

class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

