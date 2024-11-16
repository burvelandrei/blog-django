from django.test import TestCase
from .factories import UserFactory

class UserTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_user_data(self):
        self.assertTrue(self.user.username)
        self.assertTrue(self.user.email)
        self.assertTrue(self.user.birth_date)