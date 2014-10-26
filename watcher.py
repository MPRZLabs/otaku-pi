#!/usr/bin/env python2
import subprocess, os
from lib import *

def check():
	for episode in Episode.select().where(Episode.ready==True).order_by(Episode.series.asc(),Episode.order.asc()):
		print("%s" % episode)
		path = os.path.join("s%i"%episode.series.id,"e%f.mp4"%episode.order)
		if os.path.exists(path):
			subprocess.call(['omxplayer',path])
			delcode = raw_input("Delete %s from disk and database? [y/N] " % episode)
			if "y" in delcode or "Y" in delcode:
				os.remove(path)
				episode.delete_instance()
		else:
			episode.ready = False
			episode.save()

if __name__ == '__main__':
	check()
