from django import forms

from . import models


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = models.Subscribe
        fields = ['email', 'full_name']