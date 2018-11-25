from django.contrib.auth.models import User
from rest_framework import serializers

from blogs.models import Blog
from posts.models import Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('first_name', 'last_name', 'username')


class BlogListSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    count_posts = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:

        model = Blog
        fields = ('user', 'title', 'description', 'count_posts', 'url')

    def get_count_posts(self, obj):
        count_posts =  Post.objects.filter(blog_id=obj.pk).count()
        return count_posts

    def get_url(self, obj):
        url = 'http://localhost:8000/blogs/{0}'.format(obj.pk)
        return url