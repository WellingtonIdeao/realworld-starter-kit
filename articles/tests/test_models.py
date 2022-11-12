from django.test import TestCase
from django.db.models import CASCADE
from django.contrib.auth.models import User
from ..models import Article, Profile
from ..models import TEXT_MAX_LENGTH


class ArticleModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('username','test@mail.com', 'password')
        cls.article = Article.objects.create(title='title', description='description', body='body', author=user)
        
    def test_has_title(self):
        has_title = hasattr(self.article, 'title')
        self.assertTrue(has_title)

    def test_title_label(self):
        title_label = self.article._meta.get_field('title').verbose_name
        self.assertEqual(title_label, 'title')

    def test_title_max_length_is_100(self):
        title_max_length = self.article._meta.get_field('title').max_length
        self.assertEqual(title_max_length, 100)

    def test_title_is_required(self):
        title_can_empty = self.article._meta.get_field('title').blank
        self.assertEqual(title_can_empty, False)

    def test_has_description(self):
        has_description = hasattr(self.article, 'description')
        self.assertTrue(has_description)

    def test_description_label(self):
        desc_label = self.article._meta.get_field('description').verbose_name
        self.assertEqual(desc_label, 'description')

    def test_description_is_required(self):
        desc_can_empty = self.article._meta.get_field('description').blank
        self.assertEqual(desc_can_empty, False)

    def test_has_body(self):
        has_body = hasattr(self.article, 'body')
        self.assertTrue(has_body)

    def test_body_label(self):
        body_label = self.article._meta.get_field('body').verbose_name
        self.assertEqual(body_label, 'body')

    def test_body_is_required(self):
        body_can_empty = self.article._meta.get_field('body').blank
        self.assertEqual(body_can_empty, False)

    def test_has_tags(self):
        has_tags = hasattr(self.article, 'tags')
        self.assertTrue(has_tags)

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

    def test_has_createdAt(self):
        has_createdAt = hasattr(self.article, 'createdAt')
        self.assertTrue(has_createdAt)

    def test_createdAt_label(self):
        createdAt_label = self.article._meta.get_field('createdAt').verbose_name
        self.assertEqual(createdAt_label, 'createdAt')

    def test_createdAt_set_now_first_time_created(self):
        set_now_first_time_created = self.article._meta.get_field('createdAt').auto_now_add
        self.assertEqual(set_now_first_time_created, True)

    def test_has_updatedAt(self):
        has_updatedAt = hasattr(self.article, 'updatedAt')
        self.assertTrue(has_updatedAt)

    def test_updatedAt_label(self):
        updatedAt_label = self.article._meta.get_field('updatedAt').verbose_name
        self.assertEqual(updatedAt_label, 'updatedAt')

    def test_updateAt_set_now_every_time_saved(self):  
        set_now_every_time_saved = self.article._meta.get_field('updatedAt').auto_now
        self.assertEqual(set_now_every_time_saved, True)

    def test_has_favorited(self):
        has_favorited = hasattr(self.article, 'favorited')
        self.assertTrue(has_favorited)

    def test_favorited_label(self):
        favorited_label = self.article._meta.get_field('favorited').verbose_name
        self.assertEqual(favorited_label, 'favorited')

    def test_favorited_default_is_false(self):
        favorited_default = self.article._meta.get_field('favorited').default
        self.assertEqual(favorited_default, False)

    def test_has_favoritesCount(self):
        has_favoritesCount = hasattr(self.article, 'favoritesCount')
        self.assertTrue(has_favoritesCount)

    def test_favoritesCount_label(self):
        favoritesCount_label = self.article._meta.get_field('favoritesCount').verbose_name
        self.assertEqual(favoritesCount_label, 'favoritesCount')

    def test_favoritesCount_default_is_zero(self):
        favoritesCount_default = self.article._meta.get_field('favoritesCount').default
        self.assertEqual(favoritesCount_default, 0)

    def test_has_author(self):
        has_author = hasattr(self.article, 'author')
        self.assertTrue(has_author)

    def test_author_label(self):
        author_label = self.article._meta.get_field('author').verbose_name
        self.assertEqual(author_label, 'author')   

    def test_author_is_required(self):
        author_can_empty = self.article._meta.get_field('author').blank
        self.assertEqual(author_can_empty, False) 
    
    def test_author_on_delete_is_cascade(self):
        author_on_delete =  self.article._meta.get_field('author').remote_field.on_delete
        self.assertEqual(author_on_delete, CASCADE)

    def test_manager_name_for_article_backward_relationship(self):
        relation_manager_name = self.article._meta.get_field('author').remote_field.related_name
        self.assertEqual(relation_manager_name, 'articles')
    
    def test_filter_name_to_query_article_in_author(self):
        filter_name = self.article._meta.get_field('author').remote_field.related_query_name
        self.assertEqual(filter_name, 'article')

class ProfileModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('username','test@mail.com', 'password')
        cls.profile =  Profile.objects.create(author=user, bio='biography', image='https://image.jpg')

    def test_has_author(self):
        has_author = hasattr(self.profile, 'author')
        self.assertTrue(has_author)

    def test_author_label(self):
        author_label = self.profile._meta.get_field('author').verbose_name
        self.assertEqual(author_label, 'author')

    def test_manager_name_for_profile_backward_relationship(self):
        related_manager_name = self.profile._meta.get_field('author').remote_field.related_name
        self.assertEqual(related_manager_name, 'profile')

    def test_author_on_delete_is_cascade(self):
        author_on_delete =  self.profile._meta.get_field('author').remote_field.on_delete
        self.assertEqual(author_on_delete, CASCADE)

    def test_has_bio(self):
        has_bio = hasattr(self.profile, 'bio')
        self.assertTrue(has_bio)

    def test_bio_label(self):
        bio_label = self.profile._meta.get_field('bio').verbose_name
        self.assertEqual(bio_label, 'bio')
     
    def test_bio_is_required(self):
        bio_can_empty = self.profile._meta.get_field('bio').blank
        self.assertEqual(bio_can_empty, False)    

    

class UserModelTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('username','test@mail.com', 'password')
        cls.profile =  Profile.objects.create(author=cls.user, bio='biography', image='https://image.jpg')

    def test_manager_name_for_profile_backward_relationship(self):
        has_manager_name_profile = hasattr(self.user, 'profile')
        self.assertTrue(has_manager_name_profile)
     



