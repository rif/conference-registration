# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PaymentPackage'
        db.create_table('payment_paymentpackage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('ICSM_price', self.gf('django.db.models.fields.IntegerField')()),
            ('PROMISE_price', self.gf('django.db.models.fields.IntegerField')()),
            ('SCAM_price', self.gf('django.db.models.fields.IntegerField')()),
            ('WSE_price', self.gf('django.db.models.fields.IntegerField')()),
            ('tutorial_price', self.gf('django.db.models.fields.IntegerField')()),
            ('ICSM_banquet_price', self.gf('django.db.models.fields.IntegerField')()),
            ('ICSM_reception_price', self.gf('django.db.models.fields.IntegerField')()),
            ('ICSM_winetasting_price', self.gf('django.db.models.fields.IntegerField')()),
            ('ICSM_proceedings_price', self.gf('django.db.models.fields.IntegerField')()),
            ('PROMISE_SCAM_dinner_price', self.gf('django.db.models.fields.IntegerField')()),
            ('PROMISE_proceedings_price', self.gf('django.db.models.fields.IntegerField')()),
            ('SCAM_proceedings_price', self.gf('django.db.models.fields.IntegerField')()),
            ('WSE_dinner_price', self.gf('django.db.models.fields.IntegerField')()),
            ('WSE_proceedings_price', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('payment', ['PaymentPackage'])

        # Adding model 'ShoppingCart'
        db.create_table('payment_shoppingcart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('ICSM', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('PROMISE', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('SCAM', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('WSE', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('tutorial', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('extra_ICSM_banquet', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('extra_ICSM_reception', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('extra_ICSM_winetasting', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('extra_ICSM_proceedings', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('extra_PROMISE_SCAM_dinner', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('extra_PROMISE_proceedings', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('extra_SCAM_proceedings', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('extra_WSE_dinner_price', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('extra_WSE_proceedings', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal('payment', ['ShoppingCart'])


    def backwards(self, orm):
        
        # Deleting model 'PaymentPackage'
        db.delete_table('payment_paymentpackage')

        # Deleting model 'ShoppingCart'
        db.delete_table('payment_shoppingcart')


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
            'ICSM': ('django.db.models.fields.SmallIntegerField', [], {}),
            'Meta': {'object_name': 'ShoppingCart'},
            'PROMISE': ('django.db.models.fields.SmallIntegerField', [], {}),
            'SCAM': ('django.db.models.fields.SmallIntegerField', [], {}),
            'WSE': ('django.db.models.fields.SmallIntegerField', [], {}),
            'extra_ICSM_banquet': ('django.db.models.fields.SmallIntegerField', [], {}),
            'extra_ICSM_proceedings': ('django.db.models.fields.SmallIntegerField', [], {}),
            'extra_ICSM_reception': ('django.db.models.fields.SmallIntegerField', [], {}),
            'extra_ICSM_winetasting': ('django.db.models.fields.SmallIntegerField', [], {}),
            'extra_PROMISE_SCAM_dinner': ('django.db.models.fields.SmallIntegerField', [], {}),
            'extra_PROMISE_proceedings': ('django.db.models.fields.SmallIntegerField', [], {}),
            'extra_SCAM_proceedings': ('django.db.models.fields.SmallIntegerField', [], {}),
            'extra_WSE_dinner_price': ('django.db.models.fields.SmallIntegerField', [], {}),
            'extra_WSE_proceedings': ('django.db.models.fields.SmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tutorial': ('django.db.models.fields.SmallIntegerField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['payment']
