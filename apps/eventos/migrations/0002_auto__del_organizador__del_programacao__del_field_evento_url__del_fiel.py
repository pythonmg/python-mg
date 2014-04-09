# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Organizador'
        db.delete_table(u'eventos_organizador')

        # Deleting model 'Programacao'
        db.delete_table(u'eventos_programacao')

        # Deleting field 'Evento.url'
        db.delete_column(u'eventos_evento', 'url')

        # Deleting field 'Evento.nome'
        db.delete_column(u'eventos_evento', 'nome')

        # Deleting field 'Evento.descricao'
        db.delete_column(u'eventos_evento', 'descricao')

        # Adding field 'Evento.titulo'
        db.add_column(u'eventos_evento', 'titulo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Evento.email'
        db.add_column(u'eventos_evento', 'email',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Evento.endereco'
        db.add_column(u'eventos_evento', 'endereco',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Evento.info'
        db.add_column(u'eventos_evento', 'info',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Evento.preco'
        db.add_column(u'eventos_evento', 'preco',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=10, decimal_places=2),
                      keep_default=False)

        # Adding field 'Evento.site'
        db.add_column(u'eventos_evento', 'site',
                      self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Evento.imagem'
        db.add_column(u'eventos_evento', 'imagem',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Removing M2M table for field organizadores on 'Evento'
        db.delete_table(db.shorten_name(u'eventos_evento_organizadores'))


        # Changing field 'Evento.data'
        db.alter_column(u'eventos_evento', 'data', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):
        # Adding model 'Organizador'
        db.create_table(u'eventos_organizador', (
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(default='membros/avatar.gif', max_length=100, blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=180)),
        ))
        db.send_create_signal(u'eventos', ['Organizador'])

        # Adding model 'Programacao'
        db.create_table(u'eventos_programacao', (
            ('evento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Evento'])),
            ('hora_inicio', self.gf('django.db.models.fields.TimeField')()),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('hora_fim', self.gf('django.db.models.fields.TimeField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'eventos', ['Programacao'])

        # Adding field 'Evento.url'
        db.add_column(u'eventos_evento', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Evento.nome'
        db.add_column(u'eventos_evento', 'nome',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Evento.descricao'
        db.add_column(u'eventos_evento', 'descricao',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Deleting field 'Evento.titulo'
        db.delete_column(u'eventos_evento', 'titulo')

        # Deleting field 'Evento.email'
        db.delete_column(u'eventos_evento', 'email')

        # Deleting field 'Evento.endereco'
        db.delete_column(u'eventos_evento', 'endereco')

        # Deleting field 'Evento.info'
        db.delete_column(u'eventos_evento', 'info')

        # Deleting field 'Evento.preco'
        db.delete_column(u'eventos_evento', 'preco')

        # Deleting field 'Evento.site'
        db.delete_column(u'eventos_evento', 'site')

        # Deleting field 'Evento.imagem'
        db.delete_column(u'eventos_evento', 'imagem')

        # Adding M2M table for field organizadores on 'Evento'
        m2m_table_name = db.shorten_name(u'eventos_evento_organizadores')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('evento', models.ForeignKey(orm[u'eventos.evento'], null=False)),
            ('organizador', models.ForeignKey(orm[u'eventos.organizador'], null=False))
        ))
        db.create_unique(m2m_table_name, ['evento_id', 'organizador_id'])


        # Changing field 'Evento.data'
        db.alter_column(u'eventos_evento', 'data', self.gf('django.db.models.fields.DateTimeField')(default=''))

    models = {
        u'eventos.evento': {
            'Meta': {'ordering': "['-data']", 'object_name': 'Evento'},
            'data': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'endereco': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'preco': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '2'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['eventos']