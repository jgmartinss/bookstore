from django.db import models

from django.utils.translation import gettext_lazy as _

from djmoney.models.fields import MoneyField
from model_utils.models import TimeStampedModel

from . import choices


class Product(TimeStampedModel):
    is_active = models.BooleanField(
        _('Is active?'),
        default=True
    )
    is_featured = models.BooleanField(
        _('Is featured?'),
        default=True
    )
    visible_where = models.PositiveSmallIntegerField(
        _('Visible where?'),
        choices=choices.VISIBLE_WHERE
    )
    price = models.DecimalField(
        _('Price'), 
        max_digits=10, 
        decimal_places=2
    )
    cost_price = models.DecimalField(
        _('Cost price'), 
        max_digits=10, 
        decimal_places=2
    )
    special_price = models.DecimalField(
        _('Special price'), 
        max_digits=10, 
        decimal_places=2
    )
    special_price_from_date = models.DateField(
        _('Special price from date'),
        blank=True,
        null=True
    )
    special_price_to_date = models.DateField(
        _('Special price to date'),
        blank=True,
        null=True
    )
    show_real_price = models.PositiveSmallIntegerField(
        _('Show real price'),
        choices=choices.SHOW_REAL_PRICE
    )
    availability_of_stock = models.PositiveSmallIntegerField(
        _('Availability of stock'),
        choices=choices.AVAILABILITY_OF_STOCK
    )
    quantity = models.PositiveIntegerField(
        _('Quantity'),
        default=0
    )
    inventory_maintenance_unit = models.PositiveIntegerField(
        _('Inventory maintenance unit'),
        default=1
    )
    quantity_out_of_stock = models.PositiveIntegerField(
        _('Quantity for item status switch to out of stock'),
        default=1
    )
    maximum_quantity_in_the_shopping_cart = models.PositiveIntegerField(
        _('MAX/Quantity in the shopping cart'),
        default=1
    )
    notify_when_stock_is_exhausted = models.BooleanField(
        _('Notify when stock is exhausted?'),
        default=True
    )
    weight = models.FloatField(
        _('Weight'),
        blank=True,
        null=True
    )
    length = models.FloatField(
        _('Length'),
        help_text=_('Measured in centimeters.')
    )
    height = models.FloatField(
        _('Height'),
        help_text=_('Measured in centimeters.')
    )
    width = models.FloatField(
        _('Width'),
        help_text=_('Measured in centimeters.')
    )

    class Meta:
        abstract = True
