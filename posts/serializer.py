from rest_framework import serializers

from blogs.models import Blog
from posts.models import Category
from posts.models import Post


class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category
        fields = '__all__'


class PostListSerializer(serializers.Serializer):

    title = serializers.CharField()
    introduction = serializers.CharField()
    url_image = serializers.CharField()
    pub_date = serializers.CharField()


class PostSerializer(PostListSerializer):

    id = serializers.ReadOnlyField()
    post_body = serializers.CharField()
    blog = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Blog.objects.all())
    category = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Category.objects.all())

    def create(self, request_data):
        post = Post()
        return self.update(post,request_data)

    def update(self, instance, request_data):
        if request_data.get('title') is not None:
            instance.title = request_data.get('title')

        if request_data.get('introduction') is not None:
            instance.introduction = request_data.get('introduction')

        if request_data.get('post_body') is not None:
            instance.post_body = request_data.get('post_body')

        if request_data.get('url_image') is not None:
            instance.url_image = request_data.get('url_image')

        if request_data.get('pub_date') is not None:
            instance.pub_date = request_data.get('pub_date')

        if request_data.get('blog') is not None:
            instance.blog = request_data.get('blog')

        if request_data.get('category') is not None:
            instance.category = request_data.get('category')

        instance.save()
        return instance
