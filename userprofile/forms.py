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
        exclude = ('user')

class StatisticsForm(forms.Form):
    icsm = forms.BooleanField(required=False)
    promise = forms.BooleanField(required=False)
    wse = forms.BooleanField(required=False)
    scam = forms.BooleanField(required=False)
    famoosr = forms.BooleanField(required=False)
    mesoa = forms.BooleanField(required=False)
    tut1 = forms.BooleanField(required=False, help_text='Refactoring for parallelism')
    tut2 = forms.BooleanField(required=False, help_text='Migrating software testing to the cloud')
    tut3 = forms.BooleanField(required=False, help_text='Teaching undergraduate software engineering')
    tut4 = forms.BooleanField(required=False, help_text='The licensing challenge')
    extra_ICSM_banquet = forms.BooleanField(required=False)
    extra_ICSM_reception = forms.BooleanField(required=False)
    extra_ICSM_winetasting = forms.BooleanField(required=False)
    extra_ICSM_proceedings = forms.BooleanField(required=False)
    extra_PROMISE_SCAM_dinner = forms.BooleanField(required=False)
    extra_PROMISE_proceedings = forms.BooleanField(required=False)
    extra_SCAM_proceedings = forms.BooleanField(required=False)
    extra_WSE_dinner_price = forms.BooleanField(required=False)
    extra_WSE_proceedings = forms.BooleanField(required=False)

class NamesForm(forms.Form):
  names = forms.CharField(max_length=300, required=False, help_text='Comma separated names or part of the names')
