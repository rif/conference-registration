# -*- coding: utf-8 -*-
import os
def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Radu Ioan Fericean', 'fericean@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'crisis_reg.sqlite'
    }
}

TIME_ZONE = 'Europe/Bucharest'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = False
USE_L10N = True

MEDIA_ROOT = rel('upload')
MEDIA_URL = '/upload/'
STATIC_ROOT = rel('static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'icsm2010info@gmail.com'
EMAIL_HOST_PASSWORD = '1csmzoio'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SECRET_KEY = '(5&$zim^!8!mdv^ug+)2m5_3mop$bslc92j#-a_ppjromurgd8'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

STATICFILES_DIRS = (
    rel('media'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'conference_registration.urls'

TEMPLATE_DIRS = (
    rel('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # 3rd party apps
    'south',
    'uni_form',
    'django_extensions',
    # my apps
    'userprofile',
    'hotels',
    'payment',
    'iphoneids',
)
