from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'bookstore.apps.accounts'

    def ready(self):
        from . import signals
