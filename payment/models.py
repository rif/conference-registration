# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from userprofile.models import Status

class PaymentPackage(models.Model):
    STATUS_CHOICES = (
           ('REG', 'Regular'),
           ('MBR', 'IEEE Member'),
           ('SFT', 'Student Fulltime'),
           ('SMB', 'Student Member')
        )
    code = models.CharField(max_length=3, choices=STATUS_CHOICES)
    conference_price = models.IntegerField()
    early = models.BooleanField()

    def __unicode__(self):
        return self.get_code_display()
