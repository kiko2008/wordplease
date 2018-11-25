from django.contrib import admin
from posts.models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'introduction', 'url_image', 'pub_date']
    list_filter = ['categorys']

    def formatted_pub_date(self, obj):
        return obj.pub_date.strftime('%d/%m/%Y %H:%M')

    fieldsets = [
        [None, {
            'fields': ['title']
        }],
        ['Información del post', {
            'fields': ['introduction', 'url_image']
        }],
        ['Fecha de publicación', {
            'fields': ['pub_date'],
            'classes': ['collapse']
        }]
    ]