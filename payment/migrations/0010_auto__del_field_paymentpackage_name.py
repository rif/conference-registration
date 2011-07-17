# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'PaymentPackage.name'
        db.delete_column('payment_paymentpackage', 'name')


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'PaymentPackage.name'
        raise RuntimeError("Cannot reverse this migration. 'PaymentPackage.name' and its values cannot be restored.")


    models = {
        'payment.paymentpackage': {
            'Meta': {'object_name': 'PaymentPackage'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'conference_price': ('django.db.models.fields.IntegerField', [], {}),
            'early': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['payment']
