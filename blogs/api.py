from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter,  OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from blogs.models import Blog
from blogs.serializer import BlogListSerializer
from posts.models import Post
from posts.serializer import PostListSerializer


class BlogViewSet(ModelViewSet):

    queryset = Blog.objects.all()

    serializer_class = BlogListSerializer
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    ordering = ['title']
    filter_fields = ['user__username']

    @action(methods=['get'], detail=True, permission_classes=[IsAuthenticatedOrReadOnly], url_path='get-posts',
            url_name='get-posts')
    def get_post(self, request, pk=None):

        # get blog with user data
        blog = get_object_or_404(Blog, pk=pk)

        view_private_post = self.request.user.is_authenticated \
            and self.request.user.is_superuser or self.request.user == blog.user

        # Filters
        blog_posts = Post.objects.filter(blog_id=pk).all()
        queryset = blog_posts if view_private_post else blog_posts.filter(status=Post.PUBLISHED).all()

        title_param = self.request.query_params.get('title', None)
        if title_param is not None:
            queryset = queryset.filter(title=title_param)

        introduction_param = self.request.query_params.get('introduction', None)
        if introduction_param is not None:
            queryset = queryset.filter(introduction=introduction_param)

        order_by = request.query_params.get('ordering', None) \
            if request.query_params.get('ordering', None) is not None else '-pub_date'


        queryset = self.paginate_queryset(queryset.order_by(order_by))
        serializer = PostListSerializer(queryset, many=True)
        return self.get_paginated_response(serializer.data)
