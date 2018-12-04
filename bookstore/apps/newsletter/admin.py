from django.contrib import admin

from . import models


class SubscribeAdmin(admin.ModelAdmin):
    model = models.Subscribe
    list_per_page = 20
    date_hierarchy = 'created'
    ordering = ('full_name', '-created',)
    search_fields = ('full_name', 'email',)
    list_display = ('email', 'full_name', 'created',)
    list_display_links = ['email']
    fieldsets = (
        (None, {
           'fields': (
               ('email', 'full_name'),
           )}
         ),
    )

admin.site.register(models.Subscribe, SubscribeAdmin)
