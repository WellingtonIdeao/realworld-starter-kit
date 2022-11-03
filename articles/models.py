from unittest.util import _MAX_LENGTH
from django.db import models
from taggit.managers import TaggableManager

MAX_LENGTH = 100

class Article(models.Model):
    title = models.CharField(max_length=MAX_LENGTH)
    description = models.TextField()
    body = models.TextField()
    tagList = TaggableManager(verbose_name="tagList",blank=True)

    def __str__(self):
        return self.title
