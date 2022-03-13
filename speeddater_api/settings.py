'''
Django settings for api project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
'''

from django.core.management.utils import get_random_secret_key
from os import environ
from os.path import join
from pathlib import Path
from speeddater_api.helpers import bcolors

# Application NAME and VERSION
APP_NAME = 'SpeedDater'
APP_VERSION = '0.6.1-alpha'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = environ['SECRET_KEY']
except KeyError:
    SECRET_KEY = get_random_secret_key()

# SECURITY WARNING: don't run with debug turned on in production!
# set DEBUG from environment variable. default to False
try:
    DEBUG = (environ['DEBUG'].lower() == 'true')
    print(f'{bcolors.WARNING}{bcolors.BOLD}***DEBUG is enabled!***{bcolors.ENDC}')
except KeyError:
    DEBUG = False

try:
    CSRF_TRUSTED_ORIGINS = environ['TRUSTED_ORIGINS'].split(',')
    # build ALLOWED_HOSTS based on CSRF_TRUSTED_ORIGINS
    ALLOWED_HOSTS = []
    for host in CSRF_TRUSTED_ORIGINS:
        # strip http:// and https://
        host = host.replace('http://', '').replace('https://', '')
        # strip port number
        host = host.split(':')[0]
        ALLOWED_HOSTS.append(host)
except KeyError:
    if not DEBUG:
        print(
            f'{bcolors.FAIL}{bcolors.BOLD}ERROR: You must configure TRUSTED_ORIGINS!{bcolors.ENDC}')
        exit(1)

# Application definition

INSTALLED_APPS = [
    # Django modules
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    # DRF modules
    'rest_framework',
    'rest_framework.authtoken',
    # our apps
    'admin_pages',
    'configuration',
    'openapi',
    'speed_dating',
    'teams',
    # Django admin module
    'django.contrib.admin',
    # django-cors module
    'corsheaders',
    # django-allauth modules
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # dj-rest-auth modules
    'dj_rest_auth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'speeddater_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'speeddater_api.context_processor.global_tags',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'speeddater_api.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# configure database from environment variable
try:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.' + environ['DATABASE_TYPE'],
            'NAME': environ['DATABASE_NAME'],
            'HOST': environ.get('DATABASE_HOST'),
            'PORT': environ.get('DATABASE_PORT'),
            'USER': environ.get('DATABASE_USERNAME'),
            'PASSWORD': environ.get('DATABASE_PASSWORD'),
        }
    }
except KeyError:
    # use default if DB isn't configured
    print(f'{bcolors.WARNING}Database is not configured! Continuing with default database settings...{bcolors.ENDC}')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }

# Authentication backends
# https://docs.djangoproject.com/en/4.0/ref/settings/#authentication-backends

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Detroit'
USE_I18N = False
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Support reverse proxy headers
# https://docs.djangoproject.com/en/4.0/ref/settings/#secure-proxy-ssl-header

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Use Django authentication pages
# https://docs.djangoproject.com/en/4.0/ref/settings/#login-url

LOGIN_REDIRECT_URL = '/'

# django-allauth and dj-rest-auth
# https://dj-rest-auth.readthedocs.io/en/latest/installation.html

SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_PASSWORD_MIN_LENGTH = 8
SOCIALACCOUNT_ADAPTER = 'speeddater_api.allauth.adapters.SocialEmailAsUsernameAdapter'
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_LOGIN_ON_GET = True
# configure Google OAuth credentials from environment variable
try:
    SOCIALACCOUNT_PROVIDERS = {
        'google': {
            'APP': {
                'client_id': environ['GOOGLE_OAUTH_CLIENT_ID'],
                'secret': environ['GOOGLE_OAUTH_CLIENT_SECRET'],
            }
        }
    }
    # only enable Google auth if client_id and secret are configured
    INSTALLED_APPS.append('allauth.socialaccount.providers.google')
except KeyError:
    pass

# Django REST Framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # use Django session auth and DRF token auth (Bearer header)
        'rest_framework.authentication.SessionAuthentication',
        'speeddater_api.drf_authentication.BearerAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        # only render as JSON
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        # require auth for all API endpoints by default
        'rest_framework.permissions.IsAuthenticated'
    ],
    # default to 20 items per page
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

# django-cors-headers
# https://github.com/adamchainz/django-cors-headers#configuration

# set CORS header from environment variables
try:
    CORS_ALLOWED_ORIGINS = environ['CORS_ALLOWED_ORIGINS'].split(',')
except KeyError:
    pass
