import factory
import random

from factory import fuzzy

from django.utils.text import slugify

from factory.django import DjangoModelFactory
from faker import Faker

from . import models
from . import choices

fake = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User

    email = factory.LazyAttribute(lambda a: '{}@email.com'.format(a.first_name).lower().replace(' ', ''))
    first_name = factory.Faker('name')
    last_name = factory.Faker('name')
    tax_vat_number = factory.Faker('random_number', digits=11)
    # phone_number
    company = factory.Iterator(['Campany', 'Company2', 'Company3'])
    gender = factory.Iterator(['male', 'female'])
    birthday = factory.Iterator(['1998-01-22', '1999-05-25', '1996-07-02'])
    password = factory.PostGenerationMethodCall('set_password', 'mysecret')
