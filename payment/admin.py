# -*- coding: utf-8 -*-
from django.contrib import admin
from payment.models import PaymentPackage, ShoppingCart

class PaymentPackageAdmin(admin.ModelAdmin):
    list_display = ('name', '__unicode__')
    search_fields = ['name']

def mark_paid(modeladmin, request, queryset):
    queryset.update(payment_received=True)
mark_paid.short_description = "Confirm payment for selected items"

class ShoppingCartAdmin(admin.ModelAdmin):
    search_fields = ['user__first_name', 'user__last_name']
    list_display = ('__unicode__', 'icsm_have_paper', 'wse_have_paper', 'payment_received', 'is_empty')
    list_filter = ['icsm_have_paper', 'wse_have_paper', 'payment_received']
    actions = [mark_paid]

admin.site.register(PaymentPackage, PaymentPackageAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
