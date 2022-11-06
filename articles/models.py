from unittest.util import _MAX_LENGTH
from django.db import models
from taggit.managers import TaggableManager

TEXT_MAX_LENGTH = 100

class Article(models.Model):
    title = models.CharField(max_length=TEXT_MAX_LENGTH)
    description = models.TextField()
    body = models.TextField()
    tags = TaggableManager(verbose_name="tags",blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
