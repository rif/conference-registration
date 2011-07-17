# -*- coding: utf-8 -*-
from django.contrib import admin
from payment.models import PaymentPackage

class PaymentPackageAdmin(admin.ModelAdmin):
    list_display = ('code', 'conference_price', 'early')
    search_fields = ['code']

def mark_paid(modeladmin, request, queryset):
    queryset.update(payment_received=True)
mark_paid.short_description = "Confirm payment for selected items"

admin.site.register(PaymentPackage, PaymentPackageAdmin)

