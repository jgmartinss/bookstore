ENVIRONMENT = 'development'
# ENVIRONMENT = 'production'

SETTINGS_MODULE = 'bookstore.settings.development'


if ENVIRONMENT == 'development':
    SETTINGS_MODULE = 'bookstore.settings.development'
if ENVIRONMENT == 'production':
    SETTINGS_MODULE = 'bookstore.settings.production'
