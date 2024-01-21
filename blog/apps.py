# blog/apps.py
from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        # Import SummernoteModelAdmin here to avoid "Models aren't loaded yet" issue
        from django_summernote.admin import SummernoteModelAdmin
        # Register your models with SummernoteModelAdmin here
        from .models import Post, Comment
        admin.site.register(Post, SummernoteModelAdmin)
        admin.site.register(Comment)