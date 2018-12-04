from django.db import models

from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel


class Subscribe(TimeStampedModel):
    email = models.EmailField(_('Email'), unique=True)
    full_name = models.CharField(_('Full name'), max_length=255)


    class Meta:
        app_label = 'newsletter'
        verbose_name = _("Subscribe")
        verbose_name_plural = _("Subscribes")
        db_table = 'tb_newsletter_subscribes'

    def __str__(self):
        return f"{self.email} - ({self.full_name})"
