from django.db import models

from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField
from model_utils.models import TimeStampedModel


class Address(TimeStampedModel):
    user = models.ForeignKey(
        'accounts.User',
        verbose_name=_('User'),
        related_name='user_address',
        on_delete=models.CASCADE
    )
    street_1 = models.CharField(max_length=145)
    street_2 = models.CharField(max_length=145)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    country = CountryField(blank_label='(select country)')
    postal_code = models.CharField(max_length=20)
    use_as_billing_address = models.BooleanField(
        _('Use as billing address?'),
        default=True
    )

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Address')
        db_tablespace = 'tb_customers_address'

    @property
    def streets_in_line(self):
        return f'{self.street_1} {self.street_1}'

    @property
    def region_in_line(self):
        return f'{self.city}/{self.state}/{self.country}'

    def __str__(self):
        return f"{self.get_full_name} - ({self.postal_code}/{self.street_1}, {self.street_2})"
