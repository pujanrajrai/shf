from django.contrib import admin
from .models import Blog, Comment

# Register your models here.
admin.site.register(Blog)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')

