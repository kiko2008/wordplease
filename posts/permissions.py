from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

from blogs.models import Blog
from posts.models import Post


class PostPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        blog = get_object_or_404(Blog, pk=obj.blog_id)
        return request.user.is_superuser or request.user == blog.user or obj.status == Post.PUBLISHED and view.action == 'retrieve'
