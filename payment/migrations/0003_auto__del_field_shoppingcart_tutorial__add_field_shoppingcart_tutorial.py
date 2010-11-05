# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'ShoppingCart.tutorial'
        db.delete_column('payment_shoppingcart', 'tutorial')

        # Adding field 'ShoppingCart.tutorial_refactoring_for_parallelism'
        db.add_column('payment_shoppingcart', 'tutorial_refactoring_for_parallelism', self.gf('django.db.models.fields.SmallIntegerField')(default=0), keep_default=False)

        # Adding field 'ShoppingCart.tutorial_migrating_software_testing_to_the_cloud'
        db.add_column('payment_shoppingcart', 'tutorial_migrating_software_testing_to_the_cloud', self.gf('django.db.models.fields.SmallIntegerField')(default=0), keep_default=False)

        # Adding field 'ShoppingCart.tutorial_teaching_undergraduate_software_engineering'
        db.add_column('payment_shoppingcart', 'tutorial_teaching_undergraduate_software_engineering', self.gf('django.db.models.fields.SmallIntegerField')(default=0), keep_default=False)

        # Adding field 'ShoppingCart.tutorial_the_licensing_challenge'
        db.add_column('payment_shoppingcart', 'tutorial_the_licensing_challenge', self.gf('django.db.models.fields.SmallIntegerField')(default=0), keep_default=False)

        # Deleting field 'ParticipationSurvey.tutorial3'
        db.delete_column('payment_participationsurvey', 'tutorial3')

        # Deleting field 'ParticipationSurvey.tutorial2'
        db.delete_column('payment_participationsurvey', 'tutorial2')

        # Deleting field 'ParticipationSurvey.tutorial1'
        db.delete_column('payment_participationsurvey', 'tutorial1')

        # Deleting field 'ParticipationSurvey.tutorial4'
        db.delete_column('payment_participationsurvey', 'tutorial4')


    def backwards(self, orm):
        
        # Adding field 'ShoppingCart.tutorial'
        db.add_column('payment_shoppingcart', 'tutorial', self.gf('django.db.models.fields.SmallIntegerField')(default=0), keep_default=False)

        # Deleting field 'ShoppingCart.tutorial_refactoring_for_parallelism'
        db.delete_column('payment_shoppingcart', 'tutorial_refactoring_for_parallelism')

        # Deleting field 'ShoppingCart.tutorial_migrating_software_testing_to_the_cloud'
        db.delete_column('payment_shoppingcart', 'tutorial_migrating_software_testing_to_the_cloud')

        # Deleting field 'ShoppingCart.tutorial_teaching_undergraduate_software_engineering'
        db.delete_column('payment_shoppingcart', 'tutorial_teaching_undergraduate_software_engineering')

        # Deleting field 'ShoppingCart.tutorial_the_licensing_challenge'
        db.delete_column('payment_shoppingcart', 'tutorial_the_licensing_challenge')

        # Adding field 'ParticipationSurvey.tutorial3'
        db.add_column('payment_participationsurvey', 'tutorial3', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)

        # Adding field 'ParticipationSurvey.tutorial2'
        db.add_column('payment_participationsurvey', 'tutorial2', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)

        # Adding field 'ParticipationSurvey.tutorial1'
        db.add_column('payment_participationsurvey', 'tutorial1', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)

        # Adding field 'ParticipationSurvey.tutorial4'
        db.add_column('payment_participationsurvey', 'tutorial4', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'payment.participationsurvey': {
            'FAMOOSR': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'MESOA': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'Meta': {'object_name': 'ParticipationSurvey'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'payment.paymentpackage': {
            'ICSM_banquet_price': ('django.db.models.fields.IntegerField', [], {}),
            'ICSM_price': ('django.db.models.fields.IntegerField', [], {}),
            'ICSM_proceedings_price': ('django.db.models.fields.IntegerField', [], {}),
            'ICSM_reception_price': ('django.db.models.fields.IntegerField', [], {}),
            'ICSM_winetasting_price': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'PaymentPackage'},
            'PROMISE_SCAM_dinner_price': ('django.db.models.fields.IntegerField', [], {}),
            'PROMISE_price': ('django.db.models.fields.IntegerField', [], {}),
            'PROMISE_proceedings_price': ('django.db.models.fields.IntegerField', [], {}),
            'SCAM_price': ('django.db.models.fields.IntegerField', [], {}),
            'SCAM_proceedings_price': ('django.db.models.fields.IntegerField', [], {}),
            'WSE_dinner_price': ('django.db.models.fields.IntegerField', [], {}),
            'WSE_price': ('django.db.models.fields.IntegerField', [], {}),
            'WSE_proceedings_price': ('django.db.models.fields.IntegerField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tutorial_price': ('django.db.models.fields.IntegerField', [], {})
        },
        'payment.shoppingcart': {
            'ICSM': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'Meta': {'object_name': 'ShoppingCart'},
            'PROMISE': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'SCAM': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'WSE': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'extra_ICSM_banquet': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'extra_ICSM_proceedings': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'extra_ICSM_reception': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'extra_ICSM_winetasting': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'extra_PROMISE_SCAM_dinner': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'extra_PROMISE_proceedings': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'extra_SCAM_proceedings': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'extra_WSE_dinner_price': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'extra_WSE_proceedings': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tutorial_migrating_software_testing_to_the_cloud': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'tutorial_refactoring_for_parallelism': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'tutorial_teaching_undergraduate_software_engineering': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'tutorial_the_licensing_challenge': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['payment']
