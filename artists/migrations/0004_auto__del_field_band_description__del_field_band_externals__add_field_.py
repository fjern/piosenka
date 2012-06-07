# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Band.description'
        db.delete_column('artists_band', 'description')

        # Deleting field 'Band.externals'
        db.delete_column('artists_band', 'externals')

        # Adding field 'Band.slug'
        db.add_column('artists_band', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=100, unique=True, null=True, db_index=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Band.description'
        db.add_column('artists_band', 'description', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Band.externals'
        db.add_column('artists_band', 'externals', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Deleting field 'Band.slug'
        db.delete_column('artists_band', 'slug')


    models = {
        'artists.artist': {
            'Meta': {'ordering': "['lastname', 'firstname']", 'object_name': 'Artist'},
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "'void'", 'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        },
        'artists.band': {
            'Meta': {'ordering': "['name']", 'object_name': 'Band'},
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['artists.Artist']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['artists']
