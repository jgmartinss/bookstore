from django.utils.translation import gettext_lazy as _

from bookstore.apps.catalog.models import Author


class AuthorSummary(Author):
    
    class Meta:
        proxy = True
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')
