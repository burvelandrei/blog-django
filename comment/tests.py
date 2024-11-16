from django.test import TestCase
from .factories import UserFactory, PublicationFactory, CommentFactory

class CommentTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.publication = PublicationFactory(author=self.user)
        self.comment = CommentFactory(publication=self.publication, author=self.user)

    def test_comment_data(self):
        self.assertTrue(self.comment.content)
        self.assertEqual(self.comment.publication, self.publication)
        self.assertEqual(self.comment.author, self.user)