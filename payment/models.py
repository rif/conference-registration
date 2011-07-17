# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from userprofile.models import Status

class PaymentPackage(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=3)
    conference_price = models.IntegerField()   

    def __unicode__(self):
        return self.name
