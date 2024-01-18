from django.contrib import admin
from django.urls import path, include  # Include the 'include' function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Include the 'blog.urls' patterns at the root path
]
