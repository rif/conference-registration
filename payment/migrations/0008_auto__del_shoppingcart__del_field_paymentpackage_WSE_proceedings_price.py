# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'ShoppingCart'
        db.delete_table('payment_shoppingcart')

        # Deleting field 'PaymentPackage.WSE_proceedings_price'
        db.delete_column('payment_paymentpackage', 'WSE_proceedings_price')

        # Deleting field 'PaymentPackage.ICSM_banquet_price'
        db.delete_column('payment_paymentpackage', 'ICSM_banquet_price')

        # Deleting field 'PaymentPackage.ICSM_winetasting_price'
        db.delete_column('payment_paymentpackage', 'ICSM_winetasting_price')

        # Deleting field 'PaymentPackage.SCAM_price'
        db.delete_column('payment_paymentpackage', 'SCAM_price')

        # Deleting field 'PaymentPackage.ICSM_reception_price'
        db.delete_column('payment_paymentpackage', 'ICSM_reception_price')

        # Deleting field 'PaymentPackage.tutorial_price'
        db.delete_column('payment_paymentpackage', 'tutorial_price')

        # Deleting field 'PaymentPackage.PROMISE_proceedings_price'
        db.delete_column('payment_paymentpackage', 'PROMISE_proceedings_price')

        # Deleting field 'PaymentPackage.PROMISE_SCAM_dinner_price'
        db.delete_column('payment_paymentpackage', 'PROMISE_SCAM_dinner_price')

        # Deleting field 'PaymentPackage.ICSM_proceedings_price'
        db.delete_column('payment_paymentpackage', 'ICSM_proceedings_price')

        # Deleting field 'PaymentPackage.WSE_price'
        db.delete_column('payment_paymentpackage', 'WSE_price')

        # Deleting field 'PaymentPackage.ICSM_price'
        db.delete_column('payment_paymentpackage', 'ICSM_price')

        # Deleting field 'PaymentPackage.WSE_dinner_price'
        db.delete_column('payment_paymentpackage', 'WSE_dinner_price')

        # Deleting field 'PaymentPackage.SCAM_proceedings_price'
        db.delete_column('payment_paymentpackage', 'SCAM_proceedings_price')

        # Deleting field 'PaymentPackage.PROMISE_price'
        db.delete_column('payment_paymentpackage', 'PROMISE_price')

        # Adding field 'PaymentPackage.conference_price'
        db.add_column('payment_paymentpackage', 'conference_price', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'ShoppingCart'
        db.create_table('payment_shoppingcart', (
            ('extra_WSE_dinner_price', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('SCAM', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('FAMOOSR', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('tutorial_migrating_software_testing_to_the_cloud', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('icsm_have_paper', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('extra_ICSM_banquet', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('ICSM', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('WSE', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tutorial_refactoring_for_parallelism', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('extra_ICSM_proceedings', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('extra_SCAM_proceedings', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('wse_have_paper', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('payment_received', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('extra_ICSM_reception', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('MESOA', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('tutorial_teaching_undergraduate_software_engineering', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('icsm_paper_nb', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('extra_WSE_proceedings', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('tutorial_the_licensing_challenge', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('wse_paper_nb', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('extra_ICSM_winetasting', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('PROMISE', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('extra_PROMISE_SCAM_dinner', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('extra_PROMISE_proceedings', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
        ))
        db.send_create_signal('payment', ['ShoppingCart'])

        # User chose to not deal with backwards NULL issues for 'PaymentPackage.WSE_proceedings_price'
        raise RuntimeError("Cannot reverse this migration. 'PaymentPackage.WSE_proceedings_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PaymentPackage.ICSM_banquet_price'
        raise RuntimeError("Cannot reverse this migration. 'PaymentPackage.ICSM_banquet_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PaymentPackage.ICSM_winetasting_price'
        raise RuntimeError("Cannot reverse this migration. 'PaymentPackage.ICSM_winetasting_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PaymentPackage.SCAM_price'
        raise RuntimeError("Cannot reverse this migration. 'PaymentPackage.SCAM_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PaymentPackage.ICSM_reception_price'
        raise RuntimeError("Cannot reverse this migration. 'PaymentPackage.ICSM_reception_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PaymentPackage.tutorial_price'
        raise RuntimeError("Cannot reverse this migration. 'PaymentPackage.tutorial_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PaymentPackage.PROMISE_proceedings_price'
        raise RuntimeError("Cannot reverse this migration. 'PaymentPackage.PROMISE_proceedings_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PaymentPackage.PROMISE_SCAM_dinner_price'
        raise RuntimeError("Cannot reverse this migration. 'PaymentPackage.PROMISE_SCAM_dinner_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PaymentPackage.ICSM_proceedings_price'
        raise RuntimeError("Cannot reverse this migration. 'PaymentPackage.ICSM_proceedings_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PaymentPackage.WSE_price'
        raise RuntimeError("Cannot reverse this migration. 'PaymentPackage.WSE_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PaymentPackage.ICSM_price'
        raise RuntimeError("Cannot reverse this migration. 'PaymentPackage.ICSM_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PaymentPackage.WSE_dinner_price'
        raise RuntimeError("Cannot reverse this migration. 'PaymentPackage.WSE_dinner_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PaymentPackage.SCAM_proceedings_price'
        raise RuntimeError("Cannot reverse this migration. 'PaymentPackage.SCAM_proceedings_price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'PaymentPackage.PROMISE_price'
        raise RuntimeError("Cannot reverse this migration. 'PaymentPackage.PROMISE_price' and its values cannot be restored.")

        # Deleting field 'PaymentPackage.conference_price'
        db.delete_column('payment_paymentpackage', 'conference_price')


    models = {
        'payment.paymentpackage': {
            'Meta': {'object_name': 'PaymentPackage'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'conference_price': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['payment']
