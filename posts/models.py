from django.db import models
from django.db.models import Model
from django_filters import FilterSet

from blogs.models import Blog


class Category(Model):

    name = models.CharField('Categorias', max_length=100)

    def __str__(self):
        return self.name


class Post(Model):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    introduction = models.CharField(max_length=200)
    post_body = models.TextField()
    url_image = models.CharField(max_length=100)
    url_video = models.CharField(default=None, blank=True, null=True, max_length=100)
    pub_date = models.DateTimeField('%d/%m/%Y %H:%M:%S')
    categorys = models.ManyToManyField(Category)

    def __str__(self):
        return '{0}'.format(self.title)


class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = ['title', 'introduction', ]
