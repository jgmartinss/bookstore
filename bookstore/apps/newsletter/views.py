from django.contrib import messages

from django.shortcuts import render, get_object_or_404

from django.urls import reverse_lazy

from django.utils.translation import gettext_lazy as _

from django.views.generic import ListView, DeleteView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from bookstore.apps.newsletter.forms import SubscribeForm
from bookstore.apps.newsletter.models import Subscribe


class SubscribeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Subscribe
    form_class = SubscribeForm
    template_name = "newsletter/new_subscribe.html"
    success_message = _("Newsletter created successfully!")
    success_url = reverse_lazy("newsletter:list-newsletter")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(SubscribeCreateView, self).form_valid(form)


class MyNewsletterListView(LoginRequiredMixin, ListView):
    model = Subscribe
    context_object_name = "my_newsletter"
    paginate_by = 5
    template_name = "newsletter/list_newsllater.html"

    def get_queryset(self, **kwargs):
        return Subscribe.objects.filter(created_by=self.request.user).order_by(
            "-created"
        )


class NewsletterDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Subscribe
    template_name = "partials/delete_object.html"
    success_message = _("Newsletter #%s deleted successfully!")
    success_url = reverse_lazy("newsletter:list-newsletter")

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Subscribe, id=_id)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.id)
        return super(NewsletterDeleteView, self).delete(request, *args, **kwargs)
