import factory
from .models import Publication
from users.factories import UserFactory


class PublicationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Publication

    title = factory.Faker('sentence')
    content = factory.Faker('paragraph')
    author = factory.SubFactory(UserFactory)
