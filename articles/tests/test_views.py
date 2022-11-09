from django.test import TestCase


class ArticleViewTests(TestCase):
    
    def test_get_article_list(self):
        response = self.client.get('/api/articles/')
        self.assertEqual(response.status_code, 200)