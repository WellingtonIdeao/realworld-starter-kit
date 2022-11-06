from django.test import TestCase
from .models import Article
from .models import TEXT_MAX_LENGTH


class ArticleModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Article.objects.create(title='title', description='description', body='body')

    def test_title_label(self):
        article = Article.objects.get(id=1)
        title_label = article._meta.get_field('title').verbose_name
        self.assertEqual(title_label, 'title')

    def test_title_max_length_is_100(self):
        article = Article.objects.get(id=1)
        title_max_length = article._meta.get_field('title').max_length
        self.assertEqual(title_max_length, 100)

    def test_title_is_required(self):
        article = Article.objects.get(id=1)
        title_can_empty = article._meta.get_field('title').blank
        self.assertEqual(title_can_empty, False)

    def test_description_label(self):
        article = Article.objects.get(id=1)
        desc_label = article._meta.get_field('description').verbose_name
        self.assertEqual(desc_label, 'description')

    def test_description_is_required(self):
        article = Article.objects.get(id=1)
        desc_can_empty = article._meta.get_field('description').blank
        self.assertEqual(desc_can_empty, False)

    def test_body_label(self):
        article = Article.objects.get(id=1)
        body_label = article._meta.get_field('body').verbose_name
        self.assertEqual(body_label, 'body')

    def test_body_is_required(self):
        article = Article.objects.get(id=1)
        body_can_empty = article._meta.get_field('body').blank
        self.assertEqual(body_can_empty, False)

    def test_tags_label(self):
        article = Article.objects.get(id=1)
        tagList_label = article._meta.get_field('tags').verbose_name
        self.assertEqual(tagList_label, 'tags')

    def test_tags_is_optional(self):
        article = Article.objects.get(id=1)
        tags_can_empty = article._meta.get_field('tags').blank
        self.assertEqual(tags_can_empty, True)

    def test_text_field_max_length_is_100(self):
        text_field_max_length = TEXT_MAX_LENGTH
        self.assertEqual(text_field_max_length, 100)

    def test_article_string_representation(self):
        article = Article.objects.get(id=1)
        str_repr = str(article)
        self.assertEqual(str_repr, 'title')

    def test_createdAt_label(self):
        article = Article.objects.get(id=1)
        createdAt_label = article._meta.get_field('createdAt').verbose_name
        self.assertEqual(createdAt_label, 'createdAt')

    def test_createdAt_set_now_first_time_created(self):
        article = Article.objects.get(id=1)
        set_now_first_time_created = article._meta.get_field('createdAt').auto_now_add
        self.assertEqual(set_now_first_time_created, True)

    def test_updatedAt_label(self):
        article = Article.objects.get(id=1)
        updatedAt_label = article._meta.get_field('updatedAt').verbose_name
        self.assertEqual(updatedAt_label, 'updatedAt')

    def test_updateAt_set_now_every_time_saved(self):
        article = Article.objects.get(id=1)     
        set_now_every_time_saved = article._meta.get_field('updatedAt').auto_now
        self.assertEqual(set_now_every_time_saved, True)
