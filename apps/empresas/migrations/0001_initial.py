# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Empresas'
        db.create_table(u'empresas_empresas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('cidade', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cep', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
            ('disponivel', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('interesse', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'empresas', ['Empresas'])


    def backwards(self, orm):
        # Deleting model 'Empresas'
        db.delete_table(u'empresas_empresas')


    models = {
        u'empresas.empresas': {
            'Meta': {'object_name': 'Empresas'},
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'disponivel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interesse': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['empresas']