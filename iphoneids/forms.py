# -*- coding: utf-8 -*-
from django import forms
from iphoneids.models import IphoneId

class IphoneIdForm(forms.ModelForm):
    class Meta:
        model = IphoneId
        exclude = ('user', 'processed')