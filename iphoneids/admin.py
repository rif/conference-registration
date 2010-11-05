# -*- coding: utf-8 -*-
from django.contrib import admin
from iphoneids.models import IphoneId

def mark_processed(modeladmin, request, queryset):
    queryset.update(processed=True)
mark_processed.short_description = "Mark selected items as processed"

class IphoneIdAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'processed')
    list_filter = ['processed']
    search_fields = ['device_name', 'device_id']
    actions = [mark_processed]

admin.site.register(IphoneId, IphoneIdAdmin)