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


admin.site.register(models.Address, AddressAdmin)
