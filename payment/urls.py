# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from payment import views

urlpatterns = patterns('',
    url(r'^shop/$', views.shop, name="shop"),
    url(r'^email/$', views.email, name="email"),
    url(r'^receipts/$', views.receipts, name="receipts"),
)

