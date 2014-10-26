#!/usr/bin/env python2
from peewee import *
import os.path
db = SqliteDatabase(os.path.expanduser("~/.config/animedb.sqlite"))

class Series(Model):
	name = CharField()
	def __str__(self):
		return self.name
	class Meta:
		database = db

class Episode(Model):
	series = ForeignKeyField(Series, related_name="episodes")
	order = FloatField()
	uri = TextField()
	ready = BooleanField()
	def __str__(self):
		return "%s %f" % (self.series.name, self.order)
	class Meta:
		database = db

if __name__ == "__main__":
	Series.create_table()
	Episode.create_table()
