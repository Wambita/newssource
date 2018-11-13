from unittest import TestCase
from app.models import Source
from app.requests import get_sources

class TestSource(TestCase):
    """
    This is where I will run all the tests for the sources
    """
    def setUp(self):
        """
        Function that run before each test
        """
        self.new_source = Source("buzzfeed","buzzfeed","entertainment","this is buzzfeed")

    def test_init(self):
        """
        Function to test whether the Source instance is instantiated correctly
        """

        self.assertEqual(self.new_source.id,"buzzfeed")
