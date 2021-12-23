from django.contrib import admin
from myblog.models import Post
# Register your models here.

@admin.register(Post)
class EtfAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_at', 'title']
    search_fields = ['author', 'title']
