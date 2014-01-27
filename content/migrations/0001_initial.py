# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Site'
        db.create_table(u'content_site', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.related.OneToOneField')(related_name='content', unique=True, to=orm['router.Domain'])),
            ('body', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'content', ['Site'])

        # Adding model 'Image'
        db.create_table(u'content_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'content', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Site'
        db.delete_table(u'content_site')

        # Deleting model 'Image'
        db.delete_table(u'content_image')


    models = {
        u'content.image': {
            'Meta': {'object_name': 'Image'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'content.site': {
            'Meta': {'object_name': 'Site'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'domain': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'content'", 'unique': 'True', 'to': u"orm['router.Domain']"}),
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

    complete_apps = ['content']