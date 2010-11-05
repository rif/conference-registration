# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core import validators

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    deadline = models.DateField()
    single_rooms = models.IntegerField()
    single_price = models.IntegerField()
    double_rooms = models.IntegerField()
    double_price = models.IntegerField()
    remarks = models.CharField(max_length=200, null=True, blank=True, help_text="Optional")

    def __unicode__(self):
        return self.name

    def total_room_number(self):
        return self.single_rooms + self.double_rooms

    def get_room_price(self, room_kind):
        if room_kind == "SG":
            return self.single_price
        if room_kind == "DL":
            return self.double_price

    def has_pending_reservations(self):
        return self.reservation_set.filter(processed=False).count() > 0

    def has_pending_cancellations(self):
        return self.cancellation_set.filter(processed=False).count() > 0

    class Meta:
        ordering = ['name']

class Reservation(models.Model):
    ROOM_CHOICES = (
        ('SG', 'Single'),
        ('DL', 'Double'),
    )
    user = models.OneToOneField(User, editable=False)
    hotel = models.ForeignKey(Hotel)
    room_kind = models.CharField(max_length=2, choices=ROOM_CHOICES, default="SG")
    number_of_rooms = models.SmallIntegerField(default=1, validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])
    arrival_date = models.DateField()
    departure_date = models.DateField()
    smoker_room = models.BooleanField()
    additional_remarks = models.CharField(max_length=100, null=True, blank=True, help_text="Optional")
    processed = models.BooleanField(help_text="Check this if the reservation was registered at the hotel (there is an bulk action on the outside list too).")

    def __unicode__(self):
        return "%s reservation at %s" % (self.user.get_full_name(), self.hotel)

    def get_days(self):
        delta = self.departure_date - self.arrival_date
        return delta.days

    def get_price(self):
        days = self.get_days()
        return self.number_of_rooms * (days*self.hotel.get_room_price(self.room_kind))

    def colored_number_of_rooms(self):
        if self.number_of_rooms > 1:
          return '<span style="font-weight:bold; color:red;"> %s</span>' % self.number_of_rooms
        return self.number_of_rooms
    colored_number_of_rooms.allow_tags = True

    def cancellation_message(self):
        return "Cancel %s's reservation, %d %s rooms arrival: %s, departure: %s remarks were: '%s'." % (self.user.get_full_name(),
            self.number_of_rooms, self.get_room_kind_display(), self.arrival_date, self.departure_date, self.additional_remarks)

class Cancellation(models.Model):
    hotel = models.ForeignKey(Hotel)
    message = models.CharField(max_length=200)
    cancellation_date = models.DateTimeField(auto_now_add=True, blank=True)
    processed = models.BooleanField(help_text="Check this if the cancellation was registered at the hotel (there is an bulk action on the outside list too).")

    def __unicode__(self):
        return self.message

    class Meta:
        ordering = ['-cancellation_date']
