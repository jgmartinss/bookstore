from django.contrib import admin

from django.utils.translation import gettext_lazy as _

from mptt.admin import DraggableMPTTAdmin
from image_cropping import ImageCroppingMixin

from . import models
from . import forms


class BookImagesAdmin(ImageCroppingMixin, admin.ModelAdmin):
    model = models.BookImages
    form = forms.BookImagesForm
    fieldsets = (
        (
            None,
            {"fields": ("book", "image", "list_page_cropping", "detail_page_cropping")},
        ),
    )


class BookImagesInline(ImageCroppingMixin, admin.TabularInline):
    model = models.BookImages


class CategoryAdmin(DraggableMPTTAdmin, admin.ModelAdmin):
    model = models.Category
    ordering = ("name", "-created")
    search_fields = ("name",)
    list_display = ("name",)
    list_display_links = ["name"]
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = ((None, {"fields": (("name", "slug"), "parent")}),)


class PublishingCompanyAdmin(admin.ModelAdmin):
    model = models.PublishingCompany
    ordering = ("name", "-created")
    search_fields = ("name",)
    list_display = ("name",)
    list_display_links = ["name"]
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = ((None, {"fields": (("name", "slug"),)}),)


class AuthorAdmin(admin.ModelAdmin):
    model = models.Author
    form = forms.AuthorForm
    list_per_page = 20
    ordering = ("name", "-created")
    search_fields = ("name",)
    list_display = ("name",)
    list_display_links = ["name"]
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = ((None, {"fields": (("name", "slug"), "about_of")}),)


class BookAdmin(admin.ModelAdmin):
    model = models.Book
    form = forms.BookForm
    # inlines = [BookImagesInline]
    list_per_page = 15
    save_on_top = True
    save_as = True
    ordering = ("title", "-created")
    search_fields = ("title", "original_title", "isbn")
    list_display = (
        "title",
        "isbn",
        "get_authors",
        "get_categories",
        "dimensions_of_the_book",
        "price",
        "quantity",
    )
    list_display_links = ["title"]
    list_filter = (
        "is_active",
        "is_featured",
        "availability_of_stock",
        "hardback",
        "author",
    )
    date_hierarchy = "created"
    radio_fields = {
        "availability_of_stock": admin.HORIZONTAL,
        "show_real_price": admin.HORIZONTAL,
    }
    filter_horizontal = ["author", "category"]
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        ("Product info", {"fields": (("visible_where", "is_active", "is_featured"),)}),
        (
            "Book info",
            {
                "fields": (
                    ("title", "slug"),
                    ("isbn", "publishing_company"),
                    "synopsis",
                    ("language", "num_of_pages", "hardback"),
                    ("author", "category"),
                )
            },
        ),
        (
            "Dimensions of the book",
            {"fields": (("length", "height", "width"), "weight")},
        ),
        (
            "Inventory info",
            {
                "fields": (
                    "availability_of_stock",
                    ("quantity", "notify_when_stock_is_exhausted"),
                    (
                        "inventory_maintenance_unit",
                        "quantity_out_of_stock",
                        "maximum_quantity_in_the_shopping_cart",
                    ),
                )
            },
        ),
        (
            "Prices",
            {
                "fields": (
                    "show_real_price",
                    "price",
                    "cost_price",
                    "special_price",
                    ("special_price_from_date", "special_price_to_date"),
                )
            },
        ),
    )

    def get_authors(self, obj):
        return ",\n".join([a.name for a in obj.author.all()])

    get_authors.short_description = _("Author(s)")

    def get_categories(self, obj):
        return ",\n".join([c.name for c in obj.category.all()])

    get_categories.short_description = _("Categories")


class BookReviewAdmin(admin.ModelAdmin):
    model = models.BookReview
    ordering = ("-created",)
    search_fields = ("user", "book__title")
    list_display = ("book", "get_short_comment", "user", "number_of_stars")
    list_display_links = ["book"]
    list_filter = ("number_of_stars",)
    date_hierarchy = "created"
    list_per_page = 15


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.PublishingCompany, PublishingCompanyAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.BookImages, BookImagesAdmin)
admin.site.register(models.BookReview, BookReviewAdmin)
