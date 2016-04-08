# coding:utf-8
import math
import time

count = 0

for x in xrange(1,5):
	for y in xrange(1,5):
		for z in xrange(1,5):
			if x != y and x != z and y != z:
				print x , y , z
				count += 1

print "total count = " , count				


for x in xrange(1,10000):
	i = int(math.sqrt(x + 100))
	j = int(math.sqrt(x + 268))
	if (i * i == x + 100) and (j * j == x + 268):
		print x

time = time.time()
