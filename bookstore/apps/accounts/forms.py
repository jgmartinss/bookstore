from django import forms

from django.utils.translation import gettext_lazy as _

from django.core.exceptions import ValidationError

from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UsernameField,
    ReadOnlyPasswordHashField
)

from django_countries.widgets import CountrySelectWidget

from . import models


class RegisterUserForm(UserCreationForm):
    birthday = forms.DateField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('YYYY-MM-DD'),
            }
        ),
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('password'),
                'required': True
            }
        )
    )

    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('password confirmation'),
                'required': True
            }
        )
    )

    class Meta:
        model = models.User

        fields = [
            'email', 'first_name', 'last_name', 'phone_number',
            'tax_vat_number', 'company', 'gender', 'birthday',
            'password1', 'password2'
        ]

        def clean_password(self):
            cleaned_data = self.cleaned_data
            if cleaned_data['password2'] != cleaned_data['password']:
                raise ValidationError('Password dont match')
            return cleaned_data['password2']


class LoginUserForm(AuthenticationForm):
    username = UsernameField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autofocus': True,
                'placeholder': _('email')
            }
        ),
        error_messages={
            'required': _('Please enter your email'),
            'invalid': _('Please enter your email valid')
        },
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('password')
            }
        ),
        error_messages={
            'required': _('Please enter your password'),
            'invalid': _('Please enter your password valid')
        },
    )


class AddressForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = [
            'street_1', 'street_2',
            'city', 'state',
            'country', 'postal_code'
        ]
        widgets = {
            'country': CountrySelectWidget()
        }


class AccountForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            'email', 'first_name', 'last_name', 'phone_number',
            'tax_vat_number', 'company', 'gender', 'birthday'
        ]
