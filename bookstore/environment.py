from decouple import config


if config('ENVIRONMENT') == 'dev':
    SETTINGS_MODULE = 'bookstore.settings.development'
if config('ENVIRONMENT') == 'prod':
    SETTINGS_MODULE = 'bookstore.settings.production'
