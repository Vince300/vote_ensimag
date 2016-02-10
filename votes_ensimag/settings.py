# coding=utf-8
"""
Django settings for votes_ensimag project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6+e)h3!xa3xo2a$h(qc&hkfz(c)(k*-ghiz^5qaep3l960fk88'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_ENV', 'production') == 'development'

TEMPLATE_DEBUG = False

if DEBUG:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
else:
    ALLOWED_HOSTS = ['votes.asso-ensimag.fr', 'votes.asso-ensimag.com']


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'votes',
    'bootstrap3',
    'import_export'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Authentification des votants
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend','votes_ensimag.IntranetFilterAuthBackend.IntranetFilterAuthBackend',)

ROOT_URLCONF = 'votes_ensimag.urls'

WSGI_APPLICATION = 'votes_ensimag.wsgi.application'

# Templates config
TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'votes', 'templates'),
    os.path.join(BASE_DIR, 'templates')
]

TEMPLATE_CONTEXT_PROCESSORS =[
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.debug',
    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.template.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
]

# -------------------------------------------------------------------------

# Added for Django suit

SUIT_CONFIG = {
    'ADMIN_NAME': 'Campagne Ensimag'
}

# -------------------------------------------------------------------------

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': json.loads(os.getenv('VOTE_ENSIMAG_DATABASE_URL'))
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Authentification personnalisée
LOGIN_URL = '/votes/login'
LOGIN_REDIRECT_URL = '/votes/'
LOGOUT_URL = '/votes/logout'
