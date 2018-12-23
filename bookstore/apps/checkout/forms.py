from django import forms

from django.utils.translation import gettext_lazy as _


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control text-center',
                'name': 'quantity',
                'min': '1',
                'max': '20',
                'value': '1',
                'type': 'number',
            }
        ),
        label='',
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
