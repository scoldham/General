#!/bin/python

import sys
import os.path
import json
import yaml

if len(sys.argv) != 2:
	print 'You must pass a file argument... and only a file argument'
	exit(0)

filepath = str(sys.argv[1])

if os.path.exists(filepath):
	stream = open(filepath, "r")
	print 'Here goes nothing.... trying to read yaml...'
	data = yaml.safe_load(stream)
	print "Read it.  Let's see if we can make it JSON"
	print json.dumps(data), "\n"
	#print "Printing hosts entry for scoldham2... \n", data['scoldham2mylabservercom']
	for i in data:
		print i," has ", data[i]
else:
	print('File does not exist')
