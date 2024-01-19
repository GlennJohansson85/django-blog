from django.contrib import admin
from .models import Post, Comment  # Import the Comment model

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # existing admin configuration for the Post model
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('body',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    approve_comments.short_description = 'Approve selected comments'
