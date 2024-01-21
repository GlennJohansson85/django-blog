from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        # Import necessary models here
        from .models import Post, Comment
        # Register your models with admin here
        from django.contrib import admin
        admin.site.register(Post)
        admin.site.register(Comment)