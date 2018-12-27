from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _


class SummarysConfig(AppConfig):
    name = 'summarys'
    verbose_name = _('Summarys')
