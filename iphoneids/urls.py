# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse
from iphoneids import views
from iphoneids.models import IphoneId
from iphoneids.forms import IphoneIdForm

urlpatterns = patterns('django.views.generic.create_update',
    url(r'^create/$', views.create, name='create'),
    url(r'^update/(?P<object_id>\d+)/$', 'update_object', {'form_class': IphoneIdForm, 'post_save_redirect': reverse('userprofile:home'), 'login_required': True}, name='update'),
    url(r'^delete/(?P<object_id>\d+)/$', 'delete_object', {'model': IphoneId, 'post_delete_redirect': reverse('userprofile:home'), 'login_required': True}, name='delete'),
)
