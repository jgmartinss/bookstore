from django.shortcuts import render, get_object_or_404

from django.urls import reverse_lazy

from django.utils.http import is_safe_url
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import (
    REDIRECT_FIELD_NAME,
    login as auth_login,
    logout as auth_logout
)

from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters

from . import forms
from . import models


class RegisterView(generic.CreateView):
    model = models.User
    form_class = forms.RegisterUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('base:index') 


class LoginView(generic.FormView):
    form_class = forms.LoginUserForm
    template_name = 'accounts/login.html'
    redirect_field_name = REDIRECT_FIELD_NAME
    success_url = reverse_lazy('base:index')

    @method_decorator(sensitive_post_parameters('password'))
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


class LogoutView(LoginRequiredMixin, generic.RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class AccountView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/detail.html'

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        context['user_information'] = self.get_user_information
        context['shipping_address_information'] = self.get_shipping_address_information
        context['billing_address_information'] = self.get_billing_address_information
        return context

    def get_user_information(self):
        return models.User.objects.filter(id=self.request.user.id)

    def get_shipping_address_information(self):
        return models.Address.objects.filter(user__id=self.request.user.id)[:1]

    def get_billing_address_information(self):
        return models.Address.objects.filter(user__id=self.request.user.id, is_billing_address=1)[:1]



class AddressCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Address
    form_class = forms.AddressForm
    template_name = 'accounts/new-address.html'
    success_url = reverse_lazy('accounts:list-address')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddressCreateView, self).form_valid(form)


class AddressListView(LoginRequiredMixin, generic.ListView):
    model = models.Address
    context_object_name = 'user_address'
    template_name = 'accounts/list-address.html'

    def get_queryset(self, **kwargs):
        address = models.Address.objects.all()
        return address.filter(user=self.request.user).order_by('-created')


class AccountUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.User
    form_class = forms.AccountForm
    template_name = 'accounts/edit-account.html'
    success_url = reverse_lazy('accounts:detail')

    def get_object(self):
        _token = self.kwargs.get("token")
        return get_object_or_404(models.User, token=_token)




