from datetime import datetime

import factory

from ads.models import Ad
from category.models import Category
from user.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('name')
    slug = factory.Faker('ean', length=8)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    birth_date = datetime.strptime('2000-01-01', '%Y-%m-%d').date()
    email = factory.Faker('email')


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = factory.Faker('name')
    category = factory.RelatedFactoryList(CategoryFactory)
    price = 12000
    author = factory.SubFactory(UserFactory)
