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

    original_title = factory.Faker('name')
    publishing_company = factory.SubFactory(PublishingCompanyFactory)
    isbn = factory.Faker('isbn10')
    synopsis = factory.Faker('sentence')
    num_of_pages = factory.Faker('random_number', digits=3)
    hardback = factory.Faker('boolean')
    language = factory.Iterator(['cs', 'de', 'en-us', 'es', 'pt-br', 'ru', 'tr'])
    is_active = factory.Faker('boolean')
    is_featured = factory.Faker('boolean')
    visible_where = factory.Iterator([choices.CATALOG, choices.SEARCH, choices.CATALOG_SEARCH])
    price = factory.Iterator([20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0])
    cost_price = factory.Iterator([15.0, 25.0, 35.0, 45.0, 55.0, 65.0, 75.0])
    special_price = factory.Iterator([17.0, 28.0, 32.0, 48.0, 58.0, 68.0, 78.0])
    special_price_from_date = factory.Faker('date_time_this_year')
    special_price_to_date = factory.Faker('date_time_this_year')
    show_real_price = factory.Iterator([choices.INCART , choices.SEARCH , choices.BEFOREORDER])
    availability_of_stock = factory.Iterator([choices.OFSTOCK , choices.INSTOCK])
    quantity = factory.Faker('random_number', digits=2)
    inventory_maintenance_unit = factory.Faker('random_number', digits=2)
    quantity_out_of_stock = factory.Faker('random_number', digits=2)
    maximum_quantity_in_the_shopping_cart = factory.Faker('random_number', digits=2)
    notify_when_stock_is_exhausted = factory.Faker('boolean')
    weight = factory.Faker('random_number', digits=1)
    length = factory.Faker('random_number', digits=1)
    height = factory.Faker('random_number', digits=1)
    width = factory.Faker('random_number', digits=1)
    slug = factory.LazyAttribute(lambda o: slugify(o.title))
    
    @factory.lazy_attribute
    def title(self):
        return ' '.join(fake.words(nb=3)).title()

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        categories = models.Category.objects.all()
        for category in random.choices(categories, k=random.randint(1, len(categories))):
            self.category.add(category)

    @factory.post_generation
    def author(self, create, extracted, **kwargs):
        authors = models.Author.objects.all()
        for author in random.choices(authors, k=random.randint(1, len(authors))):
            self.author.add(author)