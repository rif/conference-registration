# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from userprofile.models import Status

class PaymentPackage(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=3)
    ICSM_price = models.IntegerField()
    PROMISE_price = models.IntegerField()
    SCAM_price = models.IntegerField()
    WSE_price = models.IntegerField()
    tutorial_price = models.IntegerField()
    ICSM_banquet_price = models.IntegerField(help_text="Extra")
    ICSM_reception_price = models.IntegerField(help_text="Extra")
    ICSM_winetasting_price = models.IntegerField(help_text="Extra")
    ICSM_proceedings_price = models.IntegerField(help_text="Extra")
    PROMISE_SCAM_dinner_price = models.IntegerField(help_text="Extra")
    PROMISE_proceedings_price = models.IntegerField(help_text="Extra")
    SCAM_proceedings_price = models.IntegerField(help_text="Extra")
    WSE_dinner_price = models.IntegerField(help_text="Extra")
    WSE_proceedings_price = models.IntegerField(help_text="Extra")

    def __unicode__(self):
        return "ICSM: %d %d %d %d %d; Tuotrial: %d; PROMISE: %d %d %d; SCAM: %d %d %d; WSE: %d %d %d" % (self.ICSM_price,
                        self.ICSM_proceedings_price, self.ICSM_banquet_price, self.ICSM_reception_price, self.ICSM_winetasting_price,
                        self.tutorial_price, self.PROMISE_price, self.PROMISE_proceedings_price, self.PROMISE_SCAM_dinner_price,
                        self.SCAM_price, self.SCAM_proceedings_price, self.PROMISE_SCAM_dinner_price,
                        self.WSE_price, self.WSE_proceedings_price, self.WSE_dinner_price)

    def _get_item_price(self, item):
        ITEM_DICT = {
        "sc01": self.ICSM_price,
        "sc02": self.PROMISE_price,
        "sc03": self.SCAM_price,
        "sc04": self.WSE_price,
        "sc05": self.tutorial_price,
        "sc06": self.tutorial_price,
        "sc07": self.tutorial_price,
        "sc08": self.tutorial_price,
        "sc09": self.ICSM_banquet_price,
        "sc10": self.ICSM_reception_price,
        "sc11": self.ICSM_winetasting_price,
        "sc12": self.ICSM_proceedings_price,
        "sc13": self.PROMISE_SCAM_dinner_price,
        "sc14": self.PROMISE_proceedings_price,
        "sc15": self.SCAM_proceedings_price,
        "sc16": self.WSE_dinner_price,
        "sc17": self.WSE_proceedings_price,
        "sc18": 0,
        "sc19": 0,
        }
        return ITEM_DICT[item]


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, editable=False)
    ICSM = models.SmallIntegerField(default=0)
    PROMISE = models.SmallIntegerField(default=0)
    SCAM = models.SmallIntegerField(default=0)
    WSE = models.SmallIntegerField(default=0)
    tutorial_refactoring_for_parallelism = models.SmallIntegerField(default=0)
    tutorial_migrating_software_testing_to_the_cloud = models.SmallIntegerField(default=0)
    tutorial_teaching_undergraduate_software_engineering = models.SmallIntegerField(default=0)
    tutorial_the_licensing_challenge = models.SmallIntegerField(default=0)
    extra_ICSM_banquet = models.SmallIntegerField(default=0)
    extra_ICSM_reception = models.SmallIntegerField(default=0)
    extra_ICSM_winetasting = models.SmallIntegerField(default=0)
    extra_ICSM_proceedings = models.SmallIntegerField(default=0)
    extra_PROMISE_SCAM_dinner = models.SmallIntegerField(default=0)
    extra_PROMISE_proceedings = models.SmallIntegerField(default=0)
    extra_SCAM_proceedings = models.SmallIntegerField(default=0)
    extra_WSE_dinner_price = models.SmallIntegerField(default=0)
    extra_WSE_proceedings = models.SmallIntegerField(default=0)
    FAMOOSR = models.SmallIntegerField(default=0)
    MESOA = models.SmallIntegerField(default=0)
    payment_received = models.BooleanField()
    icsm_have_paper = models.BooleanField()
    icsm_paper_nb = models.CharField(max_length=3, null=True, blank=True)
    wse_have_paper = models.BooleanField()
    wse_paper_nb = models.CharField(max_length=3, null=True, blank=True)

    def __unicode__(self):
        return "%s's shopping cart" % self.user.get_full_name()

    def get_item_count(self, item):
        ITEM_DICT = {
        "sc01": self.ICSM,
        "sc02": self.PROMISE,
        "sc03": self.SCAM,
        "sc04": self.WSE,
        "sc05": self.tutorial_refactoring_for_parallelism,
        "sc06": self.tutorial_migrating_software_testing_to_the_cloud,
        "sc07": self.tutorial_teaching_undergraduate_software_engineering,
        "sc08": self.tutorial_the_licensing_challenge,
        "sc09": self.extra_ICSM_banquet,
        "sc10": self.extra_ICSM_reception,
        "sc11": self.extra_ICSM_winetasting,
        "sc12": self.extra_ICSM_proceedings,
        "sc13": self.extra_PROMISE_SCAM_dinner,
        "sc14": self.extra_PROMISE_proceedings,
        "sc15": self.extra_SCAM_proceedings,
        "sc16": self.extra_WSE_dinner_price,
        "sc17": self.extra_WSE_proceedings,
        "sc18": self.FAMOOSR,
        "sc19": self.MESOA
        }
        return ITEM_DICT[item]

    def get_item_price(self, item):
        category = self.user.status.get_payment_cathegory()
        if self.get_have_paper('sc01') and category == Status.REGULAR:
            category = Status.MEMBER
        if self.get_have_paper('sc01') and category == Status.STUDENT_FULL_TIME:
            category = Status.STUDENT_MEMBER

        package = PaymentPackage.objects.get(code=category)
        return package._get_item_price(item)

    def set_have_paper(self, item, value):
        if item == 'sc01': self.icsm_have_paper = value
        self.save()

    def get_have_paper(self, item):
        if item == 'sc01': return self.icsm_have_paper

    def set_paper_nb(self, item, value):
        if item == 'sc01': self.icsm_paper_nb = value
        self.save()

    def get_paper_nb(self, item):
        if item == 'sc01': return self.icsm_paper_nb

    def get_part_sum(self, item):
        return self.get_item_count(item) * self.get_item_price(item)

    def is_empty(self):
        tot_count = 0
        for item in ('sc01', 'sc02', 'sc03', 'sc04', 'sc05', 'sc06', 'sc07',
                    'sc08', 'sc09', 'sc10', 'sc11', 'sc12', 'sc13', 'sc14',
                    'sc15', 'sc16', 'sc17', 'sc19', 'sc18'):
            tot_count += self.get_item_count(item)
        return tot_count == 0
    is_empty.boolean = True

    def get_tot_sum(self):
        tot_sum = 0
        for item in ('sc01', 'sc02', 'sc03', 'sc04', 'sc05', 'sc06', 'sc07',
                    'sc08', 'sc09', 'sc10', 'sc11', 'sc12', 'sc13', 'sc14',
                    'sc15', 'sc16', 'sc17', 'sc19', 'sc18'):
            tot_sum += (self.get_item_count(item) * self.get_item_price(item))
        return tot_sum

