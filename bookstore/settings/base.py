import os

from decouple import config, Csv
from dj_database_url import parse as db_url


APP_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

PROJECT_ROOT = os.path.abspath(os.path.dirname(APP_ROOT))

SECRET_KEY = config('SECRET_KEY')

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize', 
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'crispy_forms',
    'phonenumber_field',
    'django_countries',
    'djmoney',
    'mptt',
    'trumbowyg',
    'easy_thumbnails',
    'image_cropping',
]

LOCAL_APPS = [
    'bookstore.apps.accounts',
    'bookstore.apps.catalog',
    'bookstore.apps.newsletter',
    'bookstore.apps.coupons',
    'bookstore.apps.checkout',
]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

AUTH_USER_MODEL = 'accounts.User'

AUTHENTICATION_BACKENDS = (
    ('django.contrib.auth.backends.ModelBackend'),
)

CART_SESSION_ID = 'cart'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookstore.urls'

WSGI_APPLICATION = 'bookstore.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(APP_ROOT, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'bookstore.apps.checkout.context_processors.cart',
            ],
        },
    },
]

LOCALE_PATHS = (os.path.join(APP_ROOT, 'locale'),)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 15
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

TRUMBOWYG_THUMBNAIL_SIZE = (300, 300)

TRUMBOWYG_TRANSLITERATE_FILENAME = False

from easy_thumbnails.conf import Settings as easy_thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
)
THUMBNAIL_PROCESSORS += easy_thumbnail_settings.THUMBNAIL_PROCESSORS

IMAGE_CROPPING_SIZE_WARNING = True
