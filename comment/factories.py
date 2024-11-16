import factory
from .models import Comment
from publication.factories import PublicationFactory
from users.factories import UserFactory

class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    publication = factory.SubFactory(PublicationFactory)
    content = factory.Faker('paragraph')
    author = factory.SubFactory(UserFactory)