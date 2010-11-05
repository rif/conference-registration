# -*- coding: utf-8 -*-
from django import forms
from hotels.models import Reservation

class ReservationForm(forms.ModelForm):
    ROOMS_NUMBER = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    number_of_rooms = forms.TypedChoiceField(coerce=int, choices=ROOMS_NUMBER)
    class Meta:
        model = Reservation
        exclude = ('user', 'processed')

    def clean(self):
        cleaned_data = self.cleaned_data
        hotel = cleaned_data.get("hotel")
        room_kind = cleaned_data.get("room_kind")
        arrival_date = cleaned_data.get("arrival_date")
        departure_date = cleaned_data.get("departure_date")
        number_of_rooms = cleaned_data.get("number_of_rooms")
        if room_kind == 'SG':
            if hotel and hotel.single_rooms < number_of_rooms:
                raise forms.ValidationError("No enogh single rooms avaliable at %s." % hotel)
        if room_kind == 'DL':
            if hotel and hotel.double_rooms < number_of_rooms:
                raise forms.ValidationError("No enogh double rooms avaliable at %s." % hotel)
        if  departure_date and arrival_date and departure_date <= arrival_date:
            raise forms.ValidationError("Departure date must be after arrival date. ")
        return cleaned_data


