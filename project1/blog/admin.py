from django.contrib import admin
from . models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author','update_date', 'published_date']
admin.site.register(Blog, BlogAdmin)