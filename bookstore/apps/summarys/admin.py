from django.contrib import admin
from django.db.models import Count
from bookstore.apps.catalog.models import Author, Book

from . import models


class AuthorSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'catalog/author/change_list.html'
    date_hierarchy = 'created'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        authors = Author.objects.all().order_by('name')
        response.context_data['authors'] = authors

        return response


admin.site.register(models.AuthorSummary, AuthorSummaryAdmin)
