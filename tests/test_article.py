from unittest import TestCase
from app.models import Article
from app.requests import get_articles

class TestArticle(TestCase):
    """
    This is a class which I'll use to run all the tests concerning news articles
    """

    def setUp(self):
        """
        Function to run before each test
        """
        self.new_article = Article("sam","Sam Kasyoki","Sam is bae","images/sam"," Sam has always been bae","18-10-2018","https://samisbae.com")

    def test_init(self):
        """
        Function to test whether the Article instance is instantiated correctly
        """

        self.assertEqual(self.new_article.author, "Sam Kasyoki")
