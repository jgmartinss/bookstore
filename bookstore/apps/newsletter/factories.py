import factory
import random

from factory import fuzzy

from django.utils.text import slugify

from factory.django import DjangoModelFactory

from faker import Faker

from . import models


fake = Faker()


class SubscribeFactory(DjangoModelFactory):
    class Meta:
        model = models.Subscribe

    email = factory.LazyAttribute(
        lambda a: "{}@email.com".format(a.full_name).lower().replace(" ", "")
    )
    full_name = factory.Faker("name")
