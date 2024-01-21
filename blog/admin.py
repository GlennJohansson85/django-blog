from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


class CommentAdmin(admin.ModelAdmin):
    # Add any specific configurations for the Comment model admin if needed
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)


