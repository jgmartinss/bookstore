from django.contrib import admin

from . import models


class CouponAdmin(admin.ModelAdmin):
    model = models.Coupon
    ordering = ('-created',)
    search_fields = ('code', 'discount',)
    list_display = ('code', 'discount', 'valid_from', 'valid_to', 'active')
    list_display_links = ['code']
    list_filter = ('active',)
    date_hierarchy = 'created'
    fieldsets = (
        (None, {
           'fields': (
               ('code', 'active'),
               'discount', 'valid_from', 'valid_to'
           )}
         ),
    )

admin.site.register(models.Coupon, CouponAdmin)
