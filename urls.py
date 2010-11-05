# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('conference_registration.userprofile.urls', namespace='userprofile')),
    (r'^hotels/', include('conference_registration.hotels.urls', namespace='hotels')),
    (r'^payment/', include('conference_registration.payment.urls', namespace='payment')),
    (r'^iphone/', include('conference_registration.iphoneids.urls', namespace='iphoneids')),
    (r'^admin/', include(admin.site.urls)),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$',
                            'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT}),
                            )
