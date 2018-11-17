from django.contrib import admin
from posts.models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['blog', 'title', 'introduction', 'post_body', 'url_image', 'pub_date', 'category']

