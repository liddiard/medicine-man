# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Site'
        db.create_table(u'location_site', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.related.OneToOneField')(related_name='location', unique=True, to=orm['router.Domain'])),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'location', ['Site'])

        # Adding model 'Artwork'
        db.create_table(u'location_artwork', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'location', ['Artwork'])


    def backwards(self, orm):
        # Deleting model 'Site'
        db.delete_table(u'location_site')

        # Deleting model 'Artwork'
        db.delete_table(u'location_artwork')


    models = {
        u'location.artwork': {
            'Meta': {'object_name': 'Artwork'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'location.site': {
            'Meta': {'object_name': 'Site'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'domain': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'location'", 'unique': 'True', 'to': u"orm['router.Domain']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'router.domain': {
            'Meta': {'object_name': 'Domain'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'default': "'lo'", 'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['location']