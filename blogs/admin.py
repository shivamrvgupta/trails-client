from django.contrib import admin
from .models import Blog, Newsletter
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo_main', 'title','is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_per_page = 25


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('id', 'email',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Newsletter, NewsAdmin)
