from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField
from .models import Article

class ArticleSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Article
        fields = [
            'id',
            'slug',
            'title',
            'description',
            'body',
            'tags',
            'createdAt',
            'updatedAt',
            'author'
        ]