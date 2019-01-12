from django import forms

from django.utils.translation import gettext_lazy as _

from . import models


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = models.Subscribe
        fields = ["email", "full_name"]
        labels = {"email": _("Email"), "full_name": _("Full name")}
