
#!/usr/bin/env python -u
# -*- coding: UTF-8 -*-

import sys
import os
import threading
import time

workspace = '';
userIdArray = []


# 根据文件名获取用户ID列表
def getFilesInFolder(folder): # return userId array
	result = [];
	files = os.listdir(folder);
	for file in files:
		path = os.path.join(folder, file);
		if (os.path.isfile(path) and path.endswith('.java')):
			id = file.split('_')[-1].split('.')[0];
			
			result.append(id);
	return result;

def runJava(sh):
	#print 'run:'+sh
	#lines = os.popen(sh);
	#print lines
	os.system(sh)
	#

def stopJava():

	lines = os.popen('ps -ef | grep Xmx4m | grep -v grep | grep -v \'sh -c\' |awk \'{print $2}\'');
	for pid in lines:
		pid = pid.strip();
		if pid.isdigit():
			sh = 'kill -9 ' + pid;
			os.popen(sh)


def do_work():
	userIdArray = getFilesInFolder(workspace + '/javasrc');
	print userIdArray;
	for id in userIdArray:
		for question in [1,2,3]:
			#sh = 'cd ' + workspace + '; java -Xmx4m -classpath . MyTest %s %d'%(id, question);
			sh = 'java -Xmx4m -classpath /home/test/javatestcase MyTest %s %d'%(id, question);
			print 'run thread:', sh
			thread = threading.Thread(target=runJava, args=(sh,))
			thread.start()
			for i in range(1,10):
				#print 'wait %d ...' % i
				time.sleep(1)
				if not thread.isAlive():
					break;
			if thread.isAlive():
				print 'stop thread...'
				stopJava();
				print '----------##,%s,%d,%s'%(id, question, '0(elapse>10s)')



if __name__ == "__main__":
	if len(sys.argv) == 2:
		workspace = sys.argv[1];
	else:
		workspace = '/home/test/javatestcase';
	print 'start to work...'
	do_work();
	print 'finished';
	time.sleep(5);

