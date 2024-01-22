from django.contrib import admin
from django.db import models
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_on', 'updated_on')
    search_fields = ['title']
    list_filter = ('status', 'created_on', 'updated_on', 'author')
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget},
    }

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'body', 'approved', 'created_on')
    list_filter = ('approved', 'created_on', 'author', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)