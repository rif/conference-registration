# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from countries import COUNTRY_CHOICES


class About(models.Model):
    TITLE_CHOICES = (
        ('PR', 'Prof.'),
        ('DR', 'Dr.'),
        ('MS', 'Mrs.'),
        ('MR', 'Mr.'),
    )
    user = models.OneToOneField(User, editable=False)
    title = models.CharField(max_length=2, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_position = models.CharField(max_length=50, null=True, blank=True, help_text="Optional")
    organisation = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50, null=True, blank=True, help_text="Optional")
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=50, help_text="ZIP")
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES)
    hide_email = models.BooleanField(help_text="I do NOT want my address distributed")
    vegetarian = models.BooleanField(help_text='Check this if you are a vegetarian. If you have any other food preferences, please write them in the "Other special needs" field below.')
    other_special_needs = models.TextField(null=True, blank=True, help_text="Please specify here any special needs that you might have concerning food (e.g. you are eating Halal or Kosher etc.) transportation, accommodation, or anything else that is in particular important for you. We will do our best to take into account all your special needs. (Optional)")

    def __unicode__(self):
        return "About " + self.user.get_full_name()

    class Meta:
        verbose_name = "User profile"
        verbose_name_plural = "Users profile"

class Accomodation(models.Model):
    user = models.OneToOneField(User, editable=False)
    arrival_date = models.DateField(null=True, blank=True, help_text="Optional")
    arrival_time = models.TimeField(null=True, blank=True, help_text="HH:MM (Optional)")
    departure_date = models.DateField(null=True, blank=True, help_text="Optional")

    def __unicode__(self):
        return "Accomodation data for " + self.user.get_full_name()

    def get_user_name(self):
        return self.user.get_full_name()

class Status(models.Model):
    REGULAR = 'REG'
    MEMBER = 'MBR'
    STUDENT_FULL_TIME = 'SFT'
    STUDENT_MEMBER = 'SMB'
    user = models.OneToOneField(User, editable=False)
    payment_received = models.BooleanField(default=False)
    IEEE_member_number = models.CharField(max_length="8", null=True, blank=True, validators=[validators.RegexValidator("\d{8}", "Please provide the 8 digits IEEE number.")], help_text="While no verification occurs at this time, we will check manually your IEEE number.")
    student = models.BooleanField(help_text="I am a full-time student and will provide documentary proof of that. To get the student reduced fee, please send proof of full-time student status (e.g. copy of student card) to crisis2011-info@cs.upt.ro or by fax: +40 256 244834.")

    def __unicode__(self):
        return self.user.get_full_name() + " status"

    def is_member(self):
        return self.IEEE_member_number != ''

    def is_regular_student(self):
        return self.get_payment_cathegory() in ('SFT', 'REG')

    def get_payment_cathegory(self):
        if self.student and self.is_member():
            return self.STUDENT_MEMBER
        if not self.student and self.is_member():
            return self.MEMBER
        if not self.student and not self.is_member():
            return self.REGULAR
        if self.student and not self.is_member():
            return self.STUDENT_FULL_TIME
        return -1

    class Meta:
        verbose_name = "Participant Status"
        verbose_name_plural = "Participants Status"

