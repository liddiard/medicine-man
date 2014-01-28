# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Domain', fields ['url']
        db.create_unique(u'router_domain', ['url'])


    def backwards(self, orm):
        # Removing unique constraint on 'Domain', fields ['url']
        db.delete_unique(u'router_domain', ['url'])


    models = {
        u'router.domain': {
            'Meta': {'object_name': 'Domain'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'default': "'lo'", 'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        }
    }

    complete_apps = ['router']