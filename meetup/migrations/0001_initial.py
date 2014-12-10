# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Member'
        db.create_table(u'meetup_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'meetup', ['Member'])

        # Adding model 'Social'
        db.create_table(u'meetup_social', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(related_name='other_services', to=orm['meetup.Member'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'meetup', ['Social'])

        # Adding model 'Photo'
        db.create_table(u'meetup_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('member', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['meetup.Member'], unique=True)),
            ('photo_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('highres_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('thumb_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'meetup', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'Member'
        db.delete_table(u'meetup_member')

        # Deleting model 'Social'
        db.delete_table(u'meetup_social')

        # Deleting model 'Photo'
        db.delete_table(u'meetup_photo')


    models = {
        u'meetup.member': {
            'Meta': {'object_name': 'Member'},
            'guid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'meetup.photo': {
            'Meta': {'object_name': 'Photo'},
            'highres_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['meetup.Member']", 'unique': 'True'}),
            'photo_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'thumb_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'meetup.social': {
            'Meta': {'object_name': 'Social'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'other_services'", 'to': u"orm['meetup.Member']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['meetup']