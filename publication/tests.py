from django.test import TestCase
from .factories import PublicationFactory
from users.factories import UserFactory

class PublicationTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.publication = PublicationFactory(author=self.user)

    def test_publication_data(self):
        self.assertTrue(self.publication.title)
        self.assertTrue(self.publication.content)
        self.assertEqual(self.publication.author, self.user)