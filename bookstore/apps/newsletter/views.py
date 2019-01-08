from django.shortcuts import render

from django.urls import reverse_lazy

from django.views import generic

from . import forms
from . import models


class SubscribeCreateView(generic.CreateView):
    model = models.Subscribe
    form_class = forms.SubscribeForm
    template_name = "newsletter/new-subscribe.html"
    success_url = reverse_lazy("accounts:detail")
