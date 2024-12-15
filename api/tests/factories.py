import factory
from api.models import Post
from faker import Faker

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    username = factory.Faker('user_name')
    title = factory.Faker('sentence')
    content = factory.Faker('paragraph')