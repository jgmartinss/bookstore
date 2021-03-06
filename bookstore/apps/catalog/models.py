from django.db import models
from django.db.models import Avg

from django.urls import reverse

from django.utils.translation import gettext_lazy as _

from django.template.defaultfilters import truncatechars

from mptt.models import MPTTModel, TreeForeignKey
from model_utils.models import TimeStampedModel

from bookstore.apps.catalog.abstract_models import Product, AbstractImage
from bookstore.apps.catalog.choices import NUMBER_OF_STAR, LANGUAGES


class PublishingCompany(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=255)
    slug = models.SlugField(_("Slug"), unique=True, blank=True)

    class Meta:
        app_label = "catalog"
        verbose_name = _("Publishing Company")
        verbose_name_plural = _("Publishers")
        db_table = "tb_catalog_publishing_company"

    def get_absolute_url(self):
        return reverse("catalog:publisher-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.name}"


class Author(TimeStampedModel):
    name = models.CharField(_("Name"), max_length=255)
    about_of = models.TextField(_("About"))
    slug = models.SlugField(_("Slug"), unique=True, blank=True)

    class Meta:
        app_label = "catalog"
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")
        db_table = "tb_catalog_author"

    @property
    def get_books_count(self):
        return Book.objects.filter(author=self).count()

    def get_absolute_url(self):
        return reverse("catalog:author-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.name}"


class Category(MPTTModel, TimeStampedModel):
    name = models.CharField(_("Name"), max_length=125)
    parent = TreeForeignKey(
        "self",
        verbose_name=_("Sub category"),
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(_("Slug"), unique=True, blank=True)

    class Meta:
        app_label = "catalog"
        unique_together = ("parent", "slug")
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        db_table = "tb_catalog_category"

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [i.slug for i in ancestors]
        slugs = []
        for i in range(len(ancestors)):
            slugs.append("/".join(ancestors[: i + 1]))
        return slugs

    def get_absolute_url(self):
        return reverse("catalog:category-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.name}"


class Book(Product):
    title = models.CharField(_("Title"), max_length=125)
    original_title = models.CharField(_("Original Title"), max_length=125)
    slug = models.SlugField(_("Slug"), unique=True, blank=True)
    author = models.ManyToManyField(
        "catalog.Author", verbose_name=_("Author"), related_name="book_authors"
    )
    category = models.ManyToManyField(
        "catalog.Category", verbose_name=_("Category"), related_name="book_categories"
    )
    publishing_company = models.ForeignKey(
        "catalog.PublishingCompany",
        verbose_name=_("Publishing Company"),
        related_name="book_publishing_company",
        on_delete=models.CASCADE,
    )
    isbn = models.CharField(_("ISBN"), max_length=13)
    synopsis = models.TextField(_("Synopsis"))
    num_of_pages = models.PositiveSmallIntegerField(_("Number of pages"), default=1)
    hardback = models.BooleanField(_("Hardback?"), default=False)
    language = models.CharField(_("Language"), max_length=20, choices=LANGUAGES)

    class Meta:
        app_label = "catalog"
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
        db_table = "tb_catalog_book"

    @property
    def dimensions_of_the_book(self):
        return f"{self.height}x{self.length} cm"

    @property
    def short_synopsis(self):
        return truncatechars(self.synopsis, 94)

    @property
    def get_count_reviews(self):
        return BookReview.objects.filter(book=self).count()

    @property
    def get_avg_ratings(self):
        queryset = BookReview.objects.filter(book=self)
        return int(queryset.aggregate(Avg("number_of_stars"))["number_of_stars__avg"])

    def get_absolute_url(self):
        return reverse("catalog:book-detail", kwargs={"slug": self.slug})

    def __str__(self):
        if self.original_title:
            return f"{self.title} - ({self.original_title})"
        return f"{self.title}"


class BookImages(AbstractImage):
    book = models.ForeignKey(
        "catalog.Book",
        verbose_name=_("Book"),
        related_name="+",
        on_delete=models.CASCADE,
    )

    class Meta:
        app_label = "catalog"
        verbose_name = _("Book Image")
        verbose_name_plural = _("Book Images")
        db_table = "tb_catalog_book_images"

    def get_absolute_url(self):
        return reverse("catalog:bookimages-detail", kwargs={"pk": self.id})

    def __str__(self):
        return f"{self.book.title}/ {self.id}"


class AuthorImages(AbstractImage):
    author = models.ForeignKey(
        "catalog.Author",
        verbose_name=_("Author"),
        related_name="+",
        on_delete=models.CASCADE,
    )

    class Meta:
        app_label = "catalog"
        verbose_name = _("Author Image")
        verbose_name_plural = _("Author Images")
        db_table = "tb_catalog_author_images"

    def get_absolute_url(self):
        return reverse("catalog:authorimages-detail", kwargs={"pk": self.id})

    def __str__(self):
        return f"{self.author.name}/ {self.id}"


class BookReview(TimeStampedModel):
    book = models.ForeignKey(
        "catalog.Book",
        verbose_name=_("Book"),
        related_name="book_review",
        on_delete=models.CASCADE,
    )
    comment = models.TextField(_("Comment"))
    user = models.ForeignKey(
        "accounts.User",
        verbose_name=_("User"),
        related_name="user_review",
        on_delete=models.CASCADE,
    )
    number_of_stars = models.PositiveIntegerField(
        _("Stars"), choices=NUMBER_OF_STAR, default=1
    )

    class Meta:
        app_label = "catalog"
        verbose_name = _("Book Review")
        verbose_name_plural = _("Book Reviews")
        db_table = "tb_customer_book_review"

    @property
    def get_short_comment(self):
        return truncatechars(self.comment, 45)

    def get_absolute_url(self):
        return reverse("catalog:bookreview-detail", kwargs={"pk": self.id})

    def __str__(self):
        return f"({self.book.title}) - {self.number_of_stars} Stars by: {self.user}"
