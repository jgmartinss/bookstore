import uuid

from django.db import models

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumber, PhoneNumberField

from . import managers
from . import choices


class User(AbstractBaseUser,  PermissionsMixin, TimeStampedModel):
    email = models.EmailField(_('Email'), max_length=255, unique=True)
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    tax_vat_number = models.CharField(_('TAX/Vat Number'), max_length=12)
    phone_number = PhoneNumberField(_('Phone'), unique=True)
    company = models.CharField(
        _('Company'),
        max_length=125,
        blank=True,
        null=True
    )
    gender = models.CharField(
        _('Gender'),
        max_length=6,
        choices=choices.GENDER ,
        blank=True,
        null=True
    )
    birthday = models.DateField(_('Birthday'), blank=True, null=True)
    token = models.UUIDField(blank=True, editable=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = managers.UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        app_label = 'accounts'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'tb_accounts_user'

    def get_short_name(self):
        return f"{self.email}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

    @property
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name, self.last_name}"

    def __str__(self):
        return f"{self.email}"
