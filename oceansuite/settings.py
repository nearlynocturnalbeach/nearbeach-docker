"""
Django settings for oceansuite project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
#from NearBeach import __version__ as VERSION
VERSION = "0.31.0"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv("DEBUG", False))

# Allowed Hosts
if "ALLOWED_HOSTS" in os.environ:
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(",")
else:
    ALLOWED_HOSTS = ['*']

if "CSRF_TRUSTED_URLS" in os.environ:
    CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_URLS').split(",")
else:
    CSRF_TRUSTED_ORIGINS = ['*']

# Application definition

INSTALLED_APPS = [
    'NearBeach.apps.NearBeachConfig',
    'extra.apps.ExtraConfig',
    'django_probes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oceansuite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'NearBeach.context_processors.django_version',
                'NearBeach.context_processors.nearbeach_version',
            ],
        },
    },
]

WSGI_APPLICATION = 'oceansuite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db_flatpack.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': F'django.db.backends.{os.getenv("DB_ENGINE")}',
        'HOST': os.getenv("DB_HOST"), # Or an IP Address that your DB is hosted on
        'PORT': os.getenv("DB_PORT"),
        'NAME': os.getenv("DB_DATABASE"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = os.getenv("TIMEZONE", 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PRIVATE_MEDIA_URL = '/private/'

# Check to see if we are importing AWS credentials
if "AWS_ACCESS_KEY_ID" in os.environ:
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")

# Check to see if we are importing Azure Credentials
if "AZURE_STORAGE_CONNECTION_STRING" in os.environ:
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    AZURE_STORAGE_CONTAINER_NAME = os.getenv("AZURE_STORAGE_CONTAINER_NAME")


PRIVATE_MEDIA_ROOT = '/private'
PRIVATE_MEDIA_SERVER = 'ApacheXSendfileServer'

if DEBUG:
    STATIC_URL = '/static/'
else:
    STATIC_URL = F"https://cdn.nearbeach.org/{VERSION}/"
    
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media/')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv('SMTP_EMAIL_HOST')
EMAIL_PORT = os.getenv('SMTP_EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('SMTP_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('SMTP_EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Security settings
# Log users out automatically
if "SESSION_COOKIE_AGE" in os.environ:
    SESSION_COOKIE_AGE = os.getenv('SESSION_COOKIE_AGE').split(",")

if "SESSION_SAVE_EVERY_REQUEST" in os.environ:
    SESSION_SAVE_EVERY_REQUEST = os.getenv('SESSION_SAVE_EVERY_REQUEST').split(",")

MAX_FILE_SIZE_UPLOAD = 104857600
if "MAX_FILE_SIZE_UPLOAD" in os.environ:
    MAX_FILE_SIZE_UPLOAD = os.getenv("MAX_FILE_SIZE_UPLOAD")
