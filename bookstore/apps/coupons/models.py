from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel


class Coupon(TimeStampedModel):
    code = models.CharField(_('Code'), max_length=100, unique=True)
    valid_from = models.DateTimeField(_('Valid from'))
    valid_to = models.DateTimeField(_('Valid to'))
    discount = models.IntegerField(
        _('Discount'),
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    active = models.BooleanField(_('Is Active?'))

    class Meta:
        app_label = 'coupons'
        verbose_name = _("Coupon")
        verbose_name_plural = _("Coupons")
        db_table = 'tb_coupon'

    def __str__(self):
        return f'{self.code}'
