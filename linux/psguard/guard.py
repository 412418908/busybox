#!/bin/env python -c

import os
import sys

workfolder = '/opt/software/psguard'

def readpsconfig(path):
	result = {};
	with open(path, 'r') as input:
		for line in input:
			line = line.strip();
			cols = line.split('=');
			if len(cols) == 2:
				result[cols[0].strip()] = cols[1].strip();

	return result;

def getPid(ps_filter):
	lines = os.popen(ps_filter);
	for pid in lines:
		pid = pid.strip();
		if pid.isdigit():
			return pid;
	return ''

def check_ps(psconfig):
	# check process exists
	pid = getPid(psconfig['ps_filter'])
	# if not exists, launch it
	if pid == '':
		print 'PID of %s not exists, launch it'%psconfig['name']
		cmd = 'cd %s;%s'%(psconfig['workfolder'], psconfig['start_cmd'])
		os.popen(cmd)
	else:
		print '%s is running, PID is %s'%(psconfig['name'], pid)


files = os.listdir(workfolder)
for file in files:
	if not file.endswith('.ini'):
		continue;

	path = os.path.join(workfolder, file);
	psconfig = readpsconfig(path);
	if len(psconfig) < 3:
		print 'config not correct, ignore %s'%file
		continue;
	psconfig['name'] = file;
	check_ps(psconfig);
