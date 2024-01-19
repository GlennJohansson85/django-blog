from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views

urlpatterns = [
    path('', blog_views.my_blog, name='blog'),  # Handle the root URL
    path('admin/', admin.site.urls),
]
