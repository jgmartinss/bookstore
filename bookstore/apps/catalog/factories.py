import factory
import random

from django.utils.text import slugify

from factory.django import DjangoModelFactory
from faker import Faker

from . import models
from . import choices


fake = Faker()


class PublishingCompanyFactory(DjangoModelFactory):
    class Meta:
        model = models.PublishingCompany

    slug = factory.LazyAttribute(lambda o: slugify(o.name))

    @factory.lazy_attribute
    def name(self):
        return ' '.join(fake.words(nb=3)).title()


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = models.Author

    about_of = factory.Faker('sentence')
    slug = factory.LazyAttribute(lambda o: slugify(o.name))

    @factory.lazy_attribute
    def name(self):
        return ' '.join(fake.words(nb=3)).title()


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = models.Category

    slug = factory.LazyAttribute(lambda o: slugify(o.name))

    @factory.lazy_attribute
    def name(self):
        return ' '.join(fake.words(nb=3)).title()


class BookFactory(DjangoModelFactory):
    class Meta:
        model = models.Book

    # original_title = factory.Faker('name')
    # author = factory.SubFactory(AuthorFactory)
    # publishing_company = factory.SubFactory(PublishingCompanyFactory)
    # isbn = factory.Faker('isbn10')
    # synopsis = factory.Faker('sentence')
    # num_of_pages = factory.Faker('random_number', digits=3)
    # hardback = factory.Faker('boolean')
    # language = factory.Iterator([])
    # is_active = factory.Faker('boolean')
    # is_featured = factory.Faker('boolean')
    # visible_where = factory.Iterator([])
    # price = factory.Faker('pydecimal', left_digits=2, right_digits=2, positive=True)
    # cost_price = factory.Faker('pydecimal', left_digits=2, right_digits=2, positive=True)
    # special_price = factory.Faker('date_time_this_year')
    # special_price_from_date = factory.Faker('date_time_this_year')
    # special_price_to_date = factory.Faker('date_time_this_year')
    # show_real_price = factory.Iterator([])
    # availability_of_stock = factory.Iterator([])
    # quantity = factory.Faker('random_number', digits=2)
    # inventory_maintenance_unit = factory.Faker('random_number', digits=2)
    # quantity_out_of_stock = factory.Faker('random_number', digits=2)
    # maximum_quantity_in_the_shopping_cart = factory.Faker('random_number', digits=2)
    # notify_when_stock_is_exhausted = factory.Faker('boolean')
    # weight = factory.Faker('random_number', digits=1)
    # length = factory.Faker('random_number', digits=1)
    # height = factory.Faker('random_number', digits=1)
    # width = factory.Faker('random_number', digits=1)
    # slug = factory.LazyAttribute(lambda o: slugify(o.title))
    #
    # @factory.lazy_attribute
    # def title(self):
    #     return ' '.join(fake.words(nb=3)).title()
    #
    # @factory.post_generation
    # def category(self, create, extracted, **kwargs):
    #     categories = models.Category.objects.all()
    #     for category in random.choices(categories, k=random.randint(1, len(categories))):
    #         self.categories.add(category)
