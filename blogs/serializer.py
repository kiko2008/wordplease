from blogs.models import Blog
from rest_framework import serializers


class BlogListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Blog
        fields = ('user', 'title', 'description')
