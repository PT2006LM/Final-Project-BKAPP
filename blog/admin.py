from django.contrib import admin
from blog import models


class CommentTabular(admin.TabularInline):
    model = models.Comment

class ReplyTabular(admin.TabularInline):
    model = models.Reply


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [
        CommentTabular,
    ]
    readonly_fields = ('created_at',)
    list_display = ('title', 'author', 'created_at')


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    inlines = [
        ReplyTabular,
    ]
    readonly_fields = ('created_at',)
    list_filter = ('created_at', 'blog')
    list_display = ('blog', 'created_at')


@admin.register(models.Reply)
class ReplyAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_filter = ('created_at')
    list_display = ('comment', 'created_at')