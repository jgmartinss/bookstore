import factory

from factory.django import DjangoModelFactory

from faker import Faker

from . import models

fake = Faker()


class CouponFactory(DjangoModelFactory):
    class Meta:
        model = models.Coupon

    code = factory.Faker('uuid4')
    valid_from = factory.Faker('date_time_this_year')
    valid_to = factory.Faker('date_time_this_year')
    discount = factory.Faker('random_number', digits=3)
    active = factory.Faker('boolean')
