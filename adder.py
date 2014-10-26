#!/usr/bin/env python2
from lib import *
try:
	while True:
		ser = raw_input("Series: ").strip()
		if len(ser) < 1:
			break
		try:
			series = Series.get(Series.name==ser)
		except Series.DoesNotExist:
			series = Series.create(name==ser)
		while True:
			numb = raw_input("\tEpisode #: ").strip()
			uri = raw_input("\tURL: ").strip()
			if len(numb) < 1 or len(uri) < 1:
				break
			print(Episode.create(series=series, order=float(numb), uri=uri, ready=False))
except KeyboardInterrupt:
	pass
