# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from payment import views

urlpatterns = patterns('',
    url(r'^shop/$', views.shop, name="shop"),
    url(r'^paypal/$', views.paypal, name="paypal"),
    url(r'^mod/$', views.modify, name="ajax-mod"),
    url(r'^sethavepaper/$', views.set_have_paper, name="ajax-have-paper"),
    url(r'^gethavepaper/(?P<item>sc\d{2})/$', views.get_have_paper, name="ajax-get-have-paper"),
    url(r'^setpapernb/$', views.set_paper_nb, name="ajax-set-paper-nb"),
    url(r'^getpapernb/(?P<item>sc\d{2})/$', views.get_paper_nb, name="ajax-get-paper-nb"),
    url(r'^getcount/(?P<item>sc\d{2})/$', views.get_item_count, name="ajax-item-count"),
    url(r'^partsum/(?P<item>sc\d{2})/$', views.get_part_sum, name="ajax-part-sum"),
    url(r'^totsum/$', views.get_tot_sum, name="ajax-tot-sum"),
    url(r'^email/$', views.email, name="email"),
    url(r'^receipts/$', views.receipts, name="receipts"),
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^regular/$','direct_to_template', {'template': 'paypal/regular.html'}, name="paypal-regular"),
    url(r'^member/$','direct_to_template', {'template': 'paypal/regular.html'}, name="paypal-member"),
    url(r'^studentfull/$','direct_to_template', {'template': 'paypal/regular.html'}, name="paypal-studentfull"),
    url(r'^studentmember/$','direct_to_template', {'template': 'paypal/regular.html'}, name="paypal-studentmember"),
)
