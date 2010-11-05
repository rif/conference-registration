from settings_dev import *

DEBUG = TEMPLATE_DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': '/home/icsmreg/icsmreg.db',
    }
}
"""EMAIL_HOST = 'hermes.cs.upt.ro'
EMAIL_HOST_USER = 'icsminfo'
EMAIL_HOST_PASSWORD = 'info@icsm@timi'
EMAIL_PORT = 465
EMAIL_USE_TLS = True"""

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'icsm2010info@gmail.com'
EMAIL_HOST_PASSWORD = '1csmzoio'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SERVER='registration.icsm2010.upt.ro'
MEDIA_URL = 'http://%s/static/media/' % SERVER
ADMIN_MEDIA_PREFIX = 'http://%s/static/admin/media/' % SERVER

