# -*- coding: utf-8 -*-
from django.contrib import admin
from userprofile.models import About, Accomodation, Status

class AboutAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'email', 'phone', 'vegetarian', 'country', 'other_special_needs')
    list_filter = ['vegetarian']
    search_fields = ['first_name', 'last_name']

class AccomodationAdmin(admin.ModelAdmin):
    list_display = ('get_user_name', 'arrival_date', 'departure_date')
    search_fields = ['user__first_name', 'user__last_name']


class StatusAdmin(admin.ModelAdmin):
    search_fields = ['user__first_name', 'user__last_name']
    list_display = ('__unicode__', 'IEEE_member_number', 'student')
    list_filter = ('student',)


admin.site.register(About, AboutAdmin)
admin.site.register(Accomodation, AccomodationAdmin)
admin.site.register(Status, StatusAdmin)
