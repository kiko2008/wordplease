from blogs.models import Blog
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    PUBLISHED = 'PUB'
    PUBLISHED_PENDING = 'PPU'

    STATUS = (
        (PUBLISHED, 'Published'),
        (PUBLISHED_PENDING, 'Pending published')
    )

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    introduction = models.CharField(max_length=200)
    post_body = models.TextField()
    url_image = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    status = models.CharField(max_length=3, choices=STATUS,  default=PUBLISHED)

    def __str__(self):
        return '{0}'.format(self.title)

