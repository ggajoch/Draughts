from threading import Timer
from time import sleep

import sys
print dir(sys)
print sys.path

def dupa():
	print "dupa"
	t = Timer(1,dupa)
	t.start()

dupa()
