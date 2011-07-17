import os
import sys
import site

site.addsitedir('/home/rif/.virtualenvs/crisis/lib/python2.6/site-packages/')
sys.path.append('/home/rif/conference_registration/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'conference_registration.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

