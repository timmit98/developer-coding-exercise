import unittest
from models import BlogContent
from unittest.mock import Mock, patch

from .utils.determine_tags import most_common_words
from django.test import TestCase

class DetermineTagTests(unittest.TestCase):
    def test_stop_words_not_returned(self):
        STOP_WORDS = ['blah']
        test_case = most_common_words('blah blah test', STOP_WORDS, n=1)
        self.assertNotIn('blah', test_case)

    def test_returns_most_common_words(self):
        STOP_WORDS = []
        test_case = most_common_words('one two two three three three', STOP_WORDS, n=1)
        self.assertIn('three', test_case)
    
    def test_returns_empty_list_on_empty_string(self):
        STOP_WORDS = []
        test_case = most_common_words('', STOP_WORDS, n=1)
        self.assertEqual(0, len(test_case))

    # What is the expected behaviour of 6 most common words tied???
    
    # Unsure how to set up test database for SQLLite, would like to mock a couple of tests for the post and posts endpoints
    # Could Mock BlogContent, but then we would not be calling the "Post"/"Posts" endpoints...