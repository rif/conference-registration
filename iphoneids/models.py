# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class IphoneId(models.Model):
    user = models.ForeignKey(User, editable=False)
    device_name = models.CharField(max_length=20, help_text="(e.g. ipad)")
    devcice_id = models.CharField(max_length=40)
    processed = models.BooleanField(help_text="Check this if the reservation was registered at the hotel (there is an bulk action on the outside list too).")

    def __unicode__(self):
        return "%s' %s" % (self.user.get_full_name(), self.device_name)
