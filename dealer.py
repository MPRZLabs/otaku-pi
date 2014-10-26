#!/usr/bin/env python2
import subprocess, os
from lib import *

def check():
	for episode in Episode.select().where(Episode.ready==False).order_by(Episode.series.asc(),Episode.order.asc()):
		print("%s" % episode)
		if not os.path.exists("s%i"%episode.series.id):
			os.mkdir("s%i"%episode.series.id)
		if os.path.isdir("s%i"%episode.series.id):
			if subprocess.call(['wget','-c','-O',os.path.join("s%i"%episode.series.id,"e%f.mp4"%episode.order),episode.uri]) == 0:
				if os.path.getsize(os.path.join("s%i"%episode.series.id,"e%f.mp4"%episode.order)) > 1000000:
					episode.ready = True
					episode.save()
				else:
					print("wrong size")
		else:
			print("not dir")
			continue

if __name__ == '__main__':
	check()
