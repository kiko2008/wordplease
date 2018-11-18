from blogs.models import Blog
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('first_name', 'last_name', 'username')


class BlogListSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:

        model = Blog
        fields = ('user', 'title', 'description')
