from settings_dev import *

DEBUG = TEMPLATE_DEBUG =False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/rif/db/crisis2011reg.db',
    }
}

