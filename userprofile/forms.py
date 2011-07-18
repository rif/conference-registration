# -*- coding: utf-8 -*-
from django import forms
from userprofile.models import About, Accomodation, Status

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        exclude = ('user')

class AccomodationForm(forms.ModelForm):
    class Meta:
        model = Accomodation
        exclude = ('user')
    def clean(self):
        cleaned_data = self.cleaned_data
        arrival_date = cleaned_data.get("arrival_date")
        departure_date = cleaned_data.get("departure_date")
        if departure_date and arrival_date and departure_date <= arrival_date:
            raise forms.ValidationError("Departure date must be after arrival date. ")
        return cleaned_data

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        exclude = ('user', 'payment_received')

class NamesForm(forms.Form):
    names = forms.CharField(max_length=300, required=False, help_text='Comma separated names or part of the names')
