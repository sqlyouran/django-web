# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InformationPublish'
        db.create_table(u'content_informationpublish', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('origin', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('editor', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('content', self.gf('DjangoUeditor.models.UEditorField')(null=True, blank=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'content', ['InformationPublish'])


    def backwards(self, orm):
        # Deleting model 'InformationPublish'
        db.delete_table(u'content_informationpublish')


    models = {
        u'content.informationpublish': {
            'Meta': {'object_name': 'InformationPublish'},
            'content': ('DjangoUeditor.models.UEditorField', [], {'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'editor': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['content']