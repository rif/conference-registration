# -*- coding: utf-8 -*-
from django.contrib import admin
from payment.models import PaymentPackage

class PaymentPackageAdmin(admin.ModelAdmin):
    list_display = ('code', 'conference_price', 'early')
    search_fields = ['code']

admin.site.register(PaymentPackage, PaymentPackageAdmin)

