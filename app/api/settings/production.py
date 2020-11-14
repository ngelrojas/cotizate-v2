"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import datetime
from corsheaders.defaults import default_methods
from corsheaders.defaults import default_headers
from decouple import config
from .conf_email import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
X_FRAME_OPTIONS = "Deny"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default="SECRET")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(config("DEBUG", default=0))

ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(" ")


# Application definition
APP_LOCAL = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

APP_THRIDPARTY = [
    "rest_framework",
    # "drf_yasg",
    "corsheaders",
]

APP_API = [
    "core",
    "users",
    "profiles",
    "profileAssociations",
    "profileCompanies",
    "categories",
    "campaings",
    "payments",
    "comments",
    "rewards",
    "favorites",
    "likes",
    "countries",
    "cities",
    "socialNetworks",
    "phases",
    "improvies",
    "bookMarks",
]

INSTALLED_APPS = APP_LOCAL + APP_THRIDPARTY + APP_API

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": config("SQL_ENGINE"),
        "NAME": config("SQL_DATABASE"),
        "USER": config("SQL_USER", "user"),
        "PASSWORD": config("SQL_PASSWORD", "password"),
        "HOST": config("SQL_HOST", "localhost"),
        "PORT": config("SQL_PORT", "5432"),
    }
}

# dictionary REST_FRAMEWORK
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    # "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

# CORS AND STUFF
# CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = list(default_methods)

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://cotizate.com",
    "http://www.cotizate.com",
    "http://34.71.45.26",
    "http://35.226.118.27",
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://cotizate.com",
    "http://www.cotizate.com",
    "http://34.71.45.26",
    "http://35.226.118.27",
]

# CORS_ORIGIN_REGEX_WHITELIST = (
# "http://localhost:3000",
# "http://cotizate.com",
# "http://www.cotizate.com",
# "http://34.71.45.26",
# "http://35.226.118.27",
# )

CSRF_COOKIE_NAME = "csrftoken"

CSRF_TRUSTED_ORIGINS = (
    "localhost:3000",
    "cotizate.com",
    "34.71.45.26",
    "35.226.118.27",
)

CORS_ALLOW_HEADERS = default_headers + (
    "x-xsrf-token",
    "HTTP_X_XSRF_TOKEN",
    "X-ACCESS_TOKEN",
)

# custom User
AUTH_USER_MODEL = "core.user"

# config jwt
JWT_AUTH = {
    "JWT_SECRET_KEY": SECRET_KEY,
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_EXPIRATION_DELTA": datetime.timedelta(seconds=4300),
    "JWT_ALLOW_REFRESH": False,
    "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(days=1),
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
    "JWT_AUTH_COOKIE": None,
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s.%(msecs)03d]%(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        }
    },
    "simple": {"format": "%(levelname)s %(message)s"},
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "log/cotizate_api_application.log",
            "when": "D",
            "interval": 1,
            "backupCount": 40,
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "propagate": True,
            "level": "INFO",
        },
        "app01": {
            "handlers": ["file"],
            "level": "INFO",
        },
    },
}
# config email
EMAIL_USE_TLS = EMAILUSETLS
EMAIL_USE_SSL = EMAILUSESSL
EMAIL_HOST = EMAILHOST
EMAIL_PORT = EMAILPORT
EMAIL_HOST_USER = EMAILHOSTUSER
EMAIL_HOST_PASSWORD = EMAILHOSTPASSWORD
EMAIL_BACKEND = EMAILBACKEND
DEFAULT_FROM_EMAIL = DEFAULTFROMEMAIL
URL_PRODUCTION = URLPRODUCTION
