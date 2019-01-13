from django.shortcuts import render, get_object_or_404

from django.urls import reverse_lazy

from django.utils.http import is_safe_url
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import (
    REDIRECT_FIELD_NAME,
    login as auth_login,
    logout as auth_logout,
)

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    TemplateView,
    UpdateView,
    RedirectView,
    FormView,
)

from bookstore.apps.accounts.forms import (
    RegisterUserForm,
    LoginUserForm,
    AddressForm,
    AccountForm,
)
from bookstore.apps.accounts.models import User, Address


class RegisterView(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("base:index")


class LoginView(FormView):
    form_class = LoginUserForm
    template_name = "accounts/login.html"
    redirect_field_name = REDIRECT_FIELD_NAME
    success_url = reverse_lazy("base:index")

    @method_decorator(sensitive_post_parameters("password"))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to


class LogoutView(LoginRequiredMixin, RedirectView):
    url = "/"

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class AccountUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = AccountForm
    template_name = "accounts/edit_account.html"
    success_message = _("Account edited successfully!")
    success_url = reverse_lazy("accounts:detail")

    def get_object(self):
        _token = self.kwargs.get("token")
        return get_object_or_404(User, token=_token)


class AccountView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/detail.html"

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        context["user_information"] = self.get_user_information
        context["shipping_address_information"] = self.get_shipping_address_information
        context["billing_address_information"] = self.get_billing_address_information
        return context

    def get_user_information(self):
        return User.objects.filter(id=self.request.user.id)

    def get_shipping_address_information(self):
        return Address.objects.filter(
            user__id=self.request.user.id, is_billing_address=0
        )[:1]

    def get_billing_address_information(self):
        return Address.objects.filter(
            user__id=self.request.user.id, is_billing_address=1
        )[:1]


class AddressCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Address
    form_class = AddressForm
    template_name = "accounts/new_address.html"
    success_message = _("Successfully created address!")
    success_url = reverse_lazy("accounts:list-address")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddressCreateView, self).form_valid(form)


class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    context_object_name = "user_address"
    template_name = "accounts/list_address.html"

    def get_queryset(self, **kwargs):
        return Address.objects.filter(user=self.request.user).order_by("-created")


class AddressDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Address
    template_name = "partials/delete_object.html"
    success_message = _("Address %s deleted successfully!")
    success_url = reverse_lazy("accounts:list-address")

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Address, id=_id)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.region_in_line)
        return super(AddressDeleteView, self).delete(request, *args, **kwargs)


class AddressUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Address
    form_class = AddressForm
    template_name = "accounts/edit_adddress.html"
    success_message = _("Address edited successfully!")
    success_url = reverse_lazy("accounts:list-address")

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Address, id=_id)
