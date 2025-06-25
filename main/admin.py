from django.contrib import admin
from .models import Categories, News, Comment


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name','image']

admin.site.register(Categories,CategoriesAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','publish','image','desc']

admin.site.register(News,NewsAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ["name","text"]
admin.site.register(Comment, CommentAdmin)
