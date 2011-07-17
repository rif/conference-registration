# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'PaymentPackage.early'
        db.add_column('payment_paymentpackage', 'early', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'PaymentPackage.early'
        db.delete_column('payment_paymentpackage', 'early')


    models = {
        'payment.paymentpackage': {
            'Meta': {'object_name': 'PaymentPackage'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'conference_price': ('django.db.models.fields.IntegerField', [], {}),
            'early': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['payment']
