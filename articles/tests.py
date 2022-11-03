from django.test import TestCase
from .models import Article
from .models import MAX_LENGTH

class ArticleModelTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Article.objects.create(title='title', description='descritption', body='body')
        
    def test_title_verbose_name(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article._meta.get_field('title').verbose_name, 'title')   

    def test_title_max_length_is_100(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article._meta.get_field('title').max_length, 100)

    def test_title_is_required(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article._meta.get_field('title').blank, False)

    
    def test_description_verbose_name(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article._meta.get_field('description').verbose_name, 'description')

    def test_description_is_required(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article._meta.get_field('description').blank, False)


    def test_body_verbose_name(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article._meta.get_field('body').verbose_name, 'body')
    
    def test_body_is_required(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article._meta.get_field('body').blank, False)


    def test_taglist_verbose_name(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article._meta.get_field('tagList').verbose_name, 'tagList')

    def test_tagList_is_optional(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article._meta.get_field('tagList').blank, True)
       

    def test_text_fields_max_length_is_100(self):
        self.assertEqual(MAX_LENGTH, 100) 

    def test_article_to_string(self):
        article = Article.objects.get(id=1)
        self.assertEqual(str(article), 'title')


