from blogs.models import Blog
from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Post(models.Model):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    introduction = models.CharField(max_length=200)
    post_body = models.TextField()
    url_image = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return '{0} {1} '.format(self.blog.title, self.title)
