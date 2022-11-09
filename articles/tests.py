from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article
from .models import TEXT_MAX_LENGTH


class ArticleModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('username','test@mail.com', 'password')
        cls.article = Article.objects.create(title='title', description='description', body='body', author=user)
        
    def test_title_label(self):
        title_label = self.article._meta.get_field('title').verbose_name
        self.assertEqual(title_label, 'title')

    def test_title_max_length_is_100(self):
        title_max_length = self.article._meta.get_field('title').max_length
        self.assertEqual(title_max_length, 100)

    def test_title_is_required(self):
        title_can_empty = self.article._meta.get_field('title').blank
        self.assertEqual(title_can_empty, False)

    def test_description_label(self):
        desc_label = self.article._meta.get_field('description').verbose_name
        self.assertEqual(desc_label, 'description')

    def test_description_is_required(self):
        desc_can_empty = self.article._meta.get_field('description').blank
        self.assertEqual(desc_can_empty, False)

    def test_body_label(self):
        body_label = self.article._meta.get_field('body').verbose_name
        self.assertEqual(body_label, 'body')

    def test_body_is_required(self):
        body_can_empty = self.article._meta.get_field('body').blank
        self.assertEqual(body_can_empty, False)

    def test_tags_label(self):
        tags_label = self.article._meta.get_field('tags').verbose_name
        self.assertEqual(tags_label, 'tags')

    def test_tags_is_optional(self):
        tags_can_empty = self.article._meta.get_field('tags').blank
        self.assertEqual(tags_can_empty, True)

    def test_text_field_max_length_is_100(self):
        self.assertEqual(TEXT_MAX_LENGTH, 100)

    def test_article_string_representation(self):
        self.assertEqual(str(self.article), 'title')

    def test_createdAt_label(self):
        createdAt_label = self.article._meta.get_field('createdAt').verbose_name
        self.assertEqual(createdAt_label, 'createdAt')

    def test_createdAt_set_now_first_time_created(self):
        set_now_first_time_created = self.article._meta.get_field('createdAt').auto_now_add
        self.assertEqual(set_now_first_time_created, True)

    def test_updatedAt_label(self):
        updatedAt_label = self.article._meta.get_field('updatedAt').verbose_name
        self.assertEqual(updatedAt_label, 'updatedAt')

    def test_updateAt_set_now_every_time_saved(self):  
        set_now_every_time_saved = self.article._meta.get_field('updatedAt').auto_now
        self.assertEqual(set_now_every_time_saved, True)

    def test_favorited_label(self):
        favorited_label = self.article._meta.get_field('favorited').verbose_name
        self.assertEqual(favorited_label, 'favorited')

    def test_favorited_default_is_false(self):
        favorited_default = self.article._meta.get_field('favorited').default
        self.assertEqual(favorited_default, False)

    def test_favoritesCount_label(self):
        favoritesCount_label = self.article._meta.get_field('favoritesCount').verbose_name
        self.assertEqual(favoritesCount_label, 'favoritesCount')

    def test_favoritesCount_default_is_zero(self):
        favoritesCount_default = self.article._meta.get_field('favoritesCount').default
        self.assertEqual(favoritesCount_default, 0)

    def test_author_label(self):
        author_label = self.article._meta.get_field('author').verbose_name
        self.assertEqual(author_label, 'author')   

    def test_author_is_required(self):
        author_can_empty = self.article._meta.get_field('author').blank
        self.assertEqual(author_can_empty, False) 
          
    



     



