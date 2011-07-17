# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from payment import views

urlpatterns = patterns('',
    url(r'^shop/$', views.shop, name="shop"),
    url(r'^paypal/$', views.paypal, name="paypal"),
    url(r'^email/$', views.email, name="email"),
    url(r'^receipts/$', views.receipts, name="receipts"),
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^regular/$','direct_to_template', {'template': 'paypal/regular.html'}, name="paypal-regular"),
    url(r'^member/$','direct_to_template', {'template': 'paypal/regular.html'}, name="paypal-member"),
    url(r'^studentfull/$','direct_to_template', {'template': 'paypal/regular.html'}, name="paypal-studentfull"),
    url(r'^studentmember/$','direct_to_template', {'template': 'paypal/regular.html'}, name="paypal-studentmember"),
)
