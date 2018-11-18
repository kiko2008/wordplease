from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from blogs.models import Blog
from blogs.serializer import BlogListSerializer


class BlogViewSet(ModelViewSet):

    queryset = Blog.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user__username',)
    serializer_class = BlogListSerializer
    ordering = ['title']
