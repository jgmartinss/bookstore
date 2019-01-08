from django import forms

from django.utils.translation import gettext_lazy as _

from bookstore.apps.accounts.models import Address

from . import models


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ("shipping_address", "billing_address")
        exclude = ["user", "is_billing_address"]
        widgets = {
            "shipping_address": forms.Select(
                attrs={"class": "custom-select d-block w-100"}
            ),
            "billing_address": forms.Select(
                attrs={"class": "custom-select d-block w-100"}
            ),
        }
        labels = {
            "shipping_address": _("Shipping address"),
            "billing_address": _("Billing address"),
        }

    def __init__(self, user, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields["shipping_address"].queryset = Address.objects.filter(
            user=user, is_billing_address=0
        )
        self.fields["billing_address"].queryset = Address.objects.filter(
            user=user, is_billing_address=1
        )
