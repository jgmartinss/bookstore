from django.db import models

from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel

from . import choices


class Order(TimeStampedModel):
    user = models.ForeignKey(
        "accounts.User",
        verbose_name=_("User"),
        related_name="user_order",
        on_delete=models.CASCADE,
    )
    shipping_address = models.ForeignKey(
        "accounts.Address",
        verbose_name=_("Shipping address"),
        related_name="shipping_address_order",
        on_delete=models.CASCADE,
    )
    billing_address = models.ForeignKey(
        "accounts.Address",
        verbose_name=_("Billing address"),
        related_name="billing_address_order",
        on_delete=models.CASCADE,
    )
    status = models.PositiveIntegerField(
        _("Status"), choices=choices.ORDER_STATUS, default=1, blank=True
    )

    class Meta:
        app_label = "orders"
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        db_table = "tb_orders_order"

    def to_dict_json(self):
        return {
            "user_email": self.user.email,
            "user_name": f"{self.user.first_name} {self.user.last_name}",
            "order_id": self.id,
            "order_date": self.created,
            "shipping_address": self.shipping_address,
            "billing_address": self.billing_address,
            "status": self.status,
        }

    def __str__(self):
        return f"{self.id}"


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(
        "orders.Order",
        verbose_name=_("Order"),
        related_name="order",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        "catalog.Book",
        verbose_name=_("Product"),
        related_name="order_items",
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(_("Quantity"), default=1)

    class Meta:
        app_label = "orders"
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Itens")
        db_table = "tb_orders_order_item"

    def get_cost(self):
        return self.price * self.quantity

    def to_dict_json(self):
        return {
            "product": self.product.title,
            "price_unit": self.product.price,
            "price": self.price,
            "quantity": self.quantity,
            "url": self.product.get_absolute_url,
        }

    def __str__(self):
        return "{}".format(self.id)
