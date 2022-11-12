from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

TEXT_MAX_LENGTH = 100


class Article(models.Model):
    title = models.CharField(max_length=TEXT_MAX_LENGTH)
    description = models.TextField()
    body = models.TextField()
    tags = TaggableManager(verbose_name="tags", blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    favorited = models.BooleanField(default=False)
    favoritesCount = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="articles",
        related_query_name="article"
    )

    def __str__(self):
        return self.title


class Profile(models.Model):
    author = models.OneToOneField(User, related_name='profile' ,on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.URLField()
    following = models.BooleanField(default=False)

