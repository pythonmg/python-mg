# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organizador'
        db.create_table(u'eventos_organizador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(default='membros/avatar.gif', max_length=100, blank=True)),
        ))
        db.send_create_signal(u'eventos', ['Organizador'])

        # Adding model 'Evento'
        db.create_table(u'eventos_evento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('data', self.gf('django.db.models.fields.DateTimeField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'eventos', ['Evento'])

        # Adding M2M table for field organizadores on 'Evento'
        m2m_table_name = db.shorten_name(u'eventos_evento_organizadores')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('evento', models.ForeignKey(orm[u'eventos.evento'], null=False)),
            ('organizador', models.ForeignKey(orm[u'eventos.organizador'], null=False))
        ))
        db.create_unique(m2m_table_name, ['evento_id', 'organizador_id'])

        # Adding model 'Programacao'
        db.create_table(u'eventos_programacao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('hora_inicio', self.gf('django.db.models.fields.TimeField')()),
            ('hora_fim', self.gf('django.db.models.fields.TimeField')()),
            ('evento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Evento'])),
        ))
        db.send_create_signal(u'eventos', ['Programacao'])


    def backwards(self, orm):
        # Deleting model 'Organizador'
        db.delete_table(u'eventos_organizador')

        # Deleting model 'Evento'
        db.delete_table(u'eventos_evento')

        # Removing M2M table for field organizadores on 'Evento'
        db.delete_table(db.shorten_name(u'eventos_evento_organizadores'))

        # Deleting model 'Programacao'
        db.delete_table(u'eventos_programacao')


    models = {
        u'eventos.evento': {
            'Meta': {'ordering': "['-data']", 'object_name': 'Evento'},
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizadores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['eventos.Organizador']", 'symmetrical': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'eventos.organizador': {
            'Meta': {'ordering': "['-nome']", 'object_name': 'Organizador'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'default': "'membros/avatar.gif'", 'max_length': '100', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'eventos.programacao': {
            'Meta': {'ordering': "['-evento', '-hora_inicio']", 'object_name': 'Programacao'},
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'evento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eventos.Evento']"}),
            'hora_fim': ('django.db.models.fields.TimeField', [], {}),
            'hora_inicio': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['eventos']