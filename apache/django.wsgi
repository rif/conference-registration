import os
import sys
import site

site.addsitedir('/home/horia/.virtualenvs/icsm/lib/python2.5/site-packages')
sys.path.append('/home/icsmreg/icsm_registration')

os.environ['DJANGO_SETTINGS_MODULE'] = 'icsm_registration.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

