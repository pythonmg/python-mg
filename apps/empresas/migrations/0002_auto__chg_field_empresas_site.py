# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Empresas.site'
        db.alter_column(u'empresas_empresas', 'site', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'Empresas.site'
        db.alter_column(u'empresas_empresas', 'site', self.gf('django.db.models.fields.CharField')(max_length=400, null=True))

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
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['empresas']