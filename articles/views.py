from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .models import Article
from .serializers import ArticleSerializer

class ArticleList(ListAPIView):

   queryset = Article.objects.all()
   serializer_class = ArticleSerializer

class ArticleDetail(RetrieveAPIView):

   queryset = Article.objects.all()
   serializer_class = ArticleSerializer
