from django import forms

from django.utils.translation import gettext_lazy as _

from django.core.exceptions import ValidationError

from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UsernameField,
    ReadOnlyPasswordHashField,
)

from django_countries.widgets import CountrySelectWidget

from bookstore.apps.accounts.models import User, Address


class RegisterUserForm(UserCreationForm):
    email = forms.CharField(
        label=_("Email"),
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": _("email"), "required": True}
        ),
    )
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": _("password"),
                "required": True,
            }
        ),
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": _("password confirmation"),
                "required": True,
            }
        ),
    )

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
        exclude = (
            "first_name",
            "last_name",
            "tax_vat_number",
            "phone_number",
            "company",
            "gender",
            "birthday",
            "token",
        )

        def clean_password(self):
            cleaned_data = self.cleaned_data
            if cleaned_data["password2"] != cleaned_data["password"]:
                raise ValidationError(_("Password dont match"))
            return cleaned_data["password2"]


class LoginUserForm(AuthenticationForm):
    username = UsernameField(
        label=_("Email"),
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "autofocus": True,
                "placeholder": _("email"),
            }
        ),
        error_messages={
            "required": _("Please enter your email"),
            "invalid": _("Please enter your email valid"),
        },
    )

    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": _("password")}
        ),
        error_messages={
            "required": _("Please enter your password"),
            "invalid": _("Please enter your password valid"),
        },
    )


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            "street_1",
            "street_2",
            "city",
            "state",
            "country",
            "postal_code",
            "is_billing_address",
        ]
        labels = {
            "street_1": _("Street 1"),
            "street_2": _("Street 2"),
            "city": _("City"),
            "state": _("State"),
            "country": _("Country"),
            "postal_code": _("Postal code"),
            "is_billing_address": _("Is billing address?"),
        }
        widgets = {"country": CountrySelectWidget()}


class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "tax_vat_number",
            "company",
            "gender",
            "birthday",
        ]
