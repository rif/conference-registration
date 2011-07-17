from settings_dev import *

DEBUG = TEMPLATE_DEBUG =True 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/rif/db/crisis2011reg.db',
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'icsm2010info@gmail.com'
EMAIL_HOST_PASSWORD = '1csmzoio'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
