# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib.auth.models import User
from userprofile import views
users_query = {'queryset': User.objects.all()}

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^list/$', views.restricted_object_list, users_query, name='list'),
    url(r'^user/(?P<object_id>\d+)/$', views.restricted_object_detail, users_query, name='detail'),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name="edit"),
    url(r'^names/$', views.names, name="names"),
    url(r'^cancelconfirmation/$',
        'django.views.generic.simple.direct_to_template',
        {'template': 'userprofile/cancel_confirmation.html'},
        name="cancel-confirmation"),
    url(r'^canceleverything/$', views.cancel_everything, name="cancel-everything"),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^accounts/login/$', 'login', {'template_name': 'auth/login.html'}, name='login'),
    url(r'^accounts/logout/$', 'logout', {"next_page": "/"}, name='logout'),
)
