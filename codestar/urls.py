from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views

urlpatterns = [
    path('', blog_views.my_blog, name='home'),  # Add this line for the root path
    path('blog/', blog_views.my_blog, name='blog'),
    path('admin/', admin.site.urls),
]
