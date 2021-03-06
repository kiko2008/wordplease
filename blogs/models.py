from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class Blog(Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title
