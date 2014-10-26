#!/usr/bin/env python2
from dealer import *
import time
try:
	while True:
		t = time.time()
		check()
		if time.time() - t < 300:
			time.sleep(int(305-(time.time()-t)))
except KeyboardInterrupt:
	pass
