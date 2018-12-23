import factory
import random

from factory import fuzzy

from django.utils.text import slugify

from factory.django import DjangoModelFactory

from faker import Faker

from . import models
from . import choices
from bookstore.apps.catalog.factories import BookFactory
from bookstore.apps.accounts.factories import UserFactory


fake = Faker()


class AddressFactory(DjangoModelFactory):
    class Meta:
        model = models.Address

    user = factory.SubFactory(UserFactory)
    street_1 = factory.Faker('street_address')
    city = factory.Faker('city')
    state = factory.Faker('state_abbr')
    country = factory.Faker('country_code')
    postal_code = factory.Faker('postalcode')
    use_as_billing_address = factory.Faker('boolean')

    @factory.lazy_attribute
    def street_2(self):
    	if random.choice((0, 0, 0, 1, 1)):
    		return fake.secondary_address()
    	return ''


class BookReviewFactory(DjangoModelFactory):
    class Meta:
        model = models.BookReview

    book = factory.SubFactory(BookFactory)
    comment = factory.Faker('sentence')
    user = factory.SubFactory(UserFactory)
    number_of_stars = factory.Iterator(
        [choices.ONE, choices.TWO, choices.THREE, choices.FOUR, choices.FIVE]
    )
