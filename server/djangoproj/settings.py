"""
Django settings for djangoproj project.
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent


# ------------------ SECURITY ------------------

SECRET_KEY = 'django-insecure-ccow$tz_=9%dxu4(0%^(z%nx32#s@(zt9$ih@)5l54yny)wm-0'

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    # IBM Cloud Theia Lab Host
    'ahsasanand-8000.theianext-1-labs-prod-misc-tools-us-east-0.proxy.cognitiveclass.ai',
]

CSRF_TRUSTED_ORIGINS = [
    'https://ahsasanand-8000.theianext-1-labs-prod-misc-tools-us-east-0.proxy.cognitiveclass.ai',
]


# ------------------ APPS ------------------

INSTALLED_APPS = [
    'djangoapp.apps.DjangoappConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
}

# ------------------ MIDDLEWARE ------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoproj.urls'


# ------------------ TEMPLATES ------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'frontend/build'),      # React build index.html
            os.path.join(BASE_DIR, 'frontend/static'),     # React static templates
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoproj.wsgi.application'


# ------------------ DATABASE ------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ------------------ PASSWORD VALIDATION ------------------

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


# ------------------ INTERNATIONALIZATION ------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ------------------ STATIC & MEDIA ------------------

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# React build assets
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/build/static'),
    os.path.join(BASE_DIR, 'frontend/static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ------------------ DEFAULT FIELD ------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
