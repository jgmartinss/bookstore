from django.contrib import admin

from bookstore.apps.accounts.models import User

from . import models


admin.site.register(models.Order)
admin.site.register(models.OrderItem)
