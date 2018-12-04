from django.db import models

from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel


class Order(TimeStampedModel):
    user = models.ForeignKey(
        'accounts.User',
        verbose_name=_('User'),
        on_delete=models.CASCADE
    )
    shipping_address = models.ForeignKey(
        'customers.Address',
        verbose_name=_('Shipping Address'),
        related_name='order_shipping_address',
        on_delete=models.CASCADE
    )
    billing_address = models.ForeignKey(
        'customers.Address',
        verbose_name=_('Billing Address'),
        related_name='order_billing_address',
        on_delete=models.CASCADE
    )
    # shipping_method
    # payment_method

    class Meta:
        app_label = 'orders'
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        db_table = 'tb_orders_order'

    def __str__(self):
        return f"{self.email} - ({self.full_name})"


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(
        'orders.Order',
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        'catalog.Book',
        related_name='order_items',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        app_label = 'orders'
        verbose_name = _("Order item")
        verbose_name_plural = _("Order items")
        db_table = 'tb_orders_order_item'

    def get_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return f'{self.order.id} - {self.product.title}'
