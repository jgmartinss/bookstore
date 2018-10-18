import os

from .base import *


DEBUG = True

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS.append('debug_toolbar')
INSTALLED_APPS.append('behave_django')

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware', )

STATIC_URL = '/static/'
#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
