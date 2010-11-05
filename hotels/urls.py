# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from hotels import views
from hotels.models import Hotel

hot_query = {'queryset': Hotel.objects.all()}

urlpatterns = patterns('',
    #url(r'^$', views.reservation, name="reservation"),
    #url(r'^cancel/$', views.cancel, name="cancel"),
    #url(r'^email/$', views.email, name="email"),
)

urlpatterns += patterns('django.views.generic.list_detail',
    url(r'^hotlist/$', 'object_list', hot_query, name="hot-list"),
)
