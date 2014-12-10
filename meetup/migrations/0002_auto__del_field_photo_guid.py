# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Photo.guid'
        db.delete_column(u'meetup_photo', 'guid')


    def backwards(self, orm):
        # Adding field 'Photo.guid'
        db.add_column(u'meetup_photo', 'guid',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=255, unique=True),
                      keep_default=False)


    models = {
        u'meetup.member': {
            'Meta': {'object_name': 'Member'},
            'guid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['meetup.Photo']", 'unique': 'True', 'null': 'True'})
        },
        u'meetup.photo': {
            'Meta': {'object_name': 'Photo'},
            'highres_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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