from django.contrib import admin

from . import models


class AddressAdmin(admin.ModelAdmin):
    model = models.Address

    ordering = ('user__first_name', '-created',)
    search_fields = ('user__email', 'postal_code',)
    list_display = (
        'postal_code', 'streets_in_line',
        'region_in_line', 'use_as_billing_address'
    )
    list_display_links = ['postal_code']
    list_filter = ('use_as_billing_address',)
    date_hierarchy = 'created'


class BookReviewAdmin(admin.ModelAdmin):
    model = models.BookReview
    ordering = ('-created',)
    search_fields = ('user', 'book__title',)
    list_display = ('book', 'get_short_comment', 'user', 'number_of_stars',)
    list_display_links = ['book']
    list_filter = ('number_of_stars',)
    date_hierarchy = 'created'
    list_per_page = 10


admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.BookReview, BookReviewAdmin)