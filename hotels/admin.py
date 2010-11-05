# -*- coding: utf-8 -*-
from django.contrib import admin
from hotels.models import Hotel, Reservation, Cancellation

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_room_number', 'single_rooms', 'single_price', 'double_rooms', 'double_price', 'remarks')
    search_fields = ['name']

def mark_processed(modeladmin, request, queryset):
    queryset.update(processed=True)
mark_processed.short_description = "Mark selected items as processed"

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'room_kind', 'colored_number_of_rooms', 'arrival_date', 'departure_date', 'additional_remarks', 'processed')
    list_filter = ['hotel', 'room_kind', 'processed']
    search_fields = ['user__first_name', 'user__last_name', 'hotel__name']
    actions = [mark_processed]

class CancellationAdmin(admin.ModelAdmin):
    list_display = ('message', 'hotel', 'cancellation_date', 'processed')
    list_filter = ['cancellation_date', 'processed']
    search_fields = ['message']
    actions = [mark_processed]

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Cancellation, CancellationAdmin)
