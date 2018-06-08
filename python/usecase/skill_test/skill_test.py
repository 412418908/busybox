
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os


workspace = '';
input_javaUserInfos = {} # key : userId , value: userInfo
userIdArray = []



def readOneUserInfo(line):
	cols = line.strip().split(',')
	if (len(cols) != 4):
		return None
	else:
		user = {'id': cols[0].lower(), 'name': cols[1], 'type': cols[2], 'dept': cols[3], 'scoreSpec':'', "scoreZ1":'', 
		'scoreZ2':'', 'scoreP1':'', 'scoreP2':'', 'scoreP3':''}
		return user


def readUserInfo(filepath):
	users = {}
	for line in open(filepath, 'r'):
		user = readOneUserInfo(line);
		if user == None:
			continue;
		users[user['id']] = user
		userIdArray.append(user['id'])
	return users;

# 获取目录下用户的文件
def getFilesInFolder(folder): # key: id  value: filename
	result = {};
	files = os.listdir(folder);
	for file in files:
		path = os.path.join(folder, file);
		if (os.path.isfile(path) and path.endswith('.txt')):
			id = file.split('_')[-1].split('.')[0].lower()
			print 'find file:',id, path;
			result[id] = path;
	return result;

# 读取答题卡， 返回dict, key: 第?题 , value: A/B/C/D
def readAnswerFile(filepath):
	result = {};
	with  open(filepath, 'r') as f:
		for line in f:
			cols = line.strip().split(':');
			if (len(cols) == 2):
				result[cols[0]] = cols[1].strip();
	return result;

# 取集合相同的个数
def getSameElementsInDict(dict1, dict2):
	cnt = 0;
	for id in dict1:
		val = dict1[id].strip().upper()
		val2 = dict2.get(id, '').strip().upper()
		if (val == val2):
			cnt += 1
	return cnt;

def getUserSpecScore(id, correctFiles, answerFiles):
	if (correctFiles.get(id, '') == ''):
		#print '%s spec答案不存在'%(id)
		return '答案不存在';
	if (answerFiles.get(id, '') == ''):
		#print '%s spec未交卷'%(id)
		return '未交卷';
	f1 = answerFiles[id];
	f2 = correctFiles[id];
	answers = readAnswerFile(f1);
	corrects = readAnswerFile(f2);
	##print answers

	return getSameElementsInDict(corrects, answers) * 2;

def getTotalScore(user):
	score = 0;
	if isinstance(user['scoreSpec'], int):
		score += user['scoreSpec'];
	if isinstance(user['scoreZ1'], int):
		score += user['scoreZ1'];
	if isinstance(user['scoreZ2'], int):
		score += user['scoreZ2'];
	if isinstance(user['scoreP1'], int):
		score += user['scoreP1'];
	if isinstance(user['scoreP2'], int):
		score += user['scoreP2'];
	if isinstance(user['scoreP3'], int):
		score += user['scoreP3'];
	return score;

def do_work():
	global input_javaUserInfos 

	javaCorrectFiles = {}; #key: userId, value: filepath
	javaAnswerFiles = {};
	uedCorrectFiles = {}; #key: userId, value: filepath
	uedAnswerFiles = {};
	dbaCorrectFiles = {}; #key: userId, value: filepath
	dbaAnswerFiles = {};
	#zgtScore = {}  #key : userId, value: (score1, score2)
	#javaScore = {}  #key: userId, value: (score1, score2, score3)
	print 'workspace:',workspace
	input_javaUserInfos = readUserInfo(unicode(workspace + '/input_userinfo/名单.csv', 'utf-8'));
	print '用户信息数:=', len(input_javaUserInfos)
	print '-------------------------'

	javaAnswerFiles = getFilesInFolder( workspace + '/input_spec/java/answer/'); 
	print 'java交卷数:', len(javaAnswerFiles)
	print '-------------------------'

	javaCorrectFiles = getFilesInFolder( workspace + '/input_spec/java/correct/'); 
	print 'java正确答案数:', len(javaCorrectFiles)
	print '-------------------------'

	uedAnswerFiles = getFilesInFolder( workspace + '/input_spec/ued/answer/'); 
	print 'ued交卷数:', len(uedAnswerFiles)
	print '-------------------------'

	uedCorrectFiles = getFilesInFolder( workspace + '/input_spec/ued/correct/'); 
	print 'ued正确答案数:', len(uedCorrectFiles)
	print '-------------------------'	

	dbaAnswerFiles = getFilesInFolder( workspace + '/input_spec/dba/answer/'); 
	print 'dba交卷数:', len(dbaAnswerFiles)
	print '-------------------------'

	dbaCorrectFiles = getFilesInFolder( workspace + '/input_spec/dba/correct/'); 
	print 'dba正确答案数:', len(dbaCorrectFiles)
	print '-------------------------'	
	
	with open(workspace + '/output_specScore/java得分.csv', 'w') as f:
		for item in input_javaUserInfos.items():
			id, userInfo = item
			if (userInfo['type'] != 'java'):
				continue;
			score = getUserSpecScore(id, javaCorrectFiles, javaAnswerFiles);
			userInfo['scoreSpec'] = score;
			line = '%s,%s,%s,%s,%s' % (id, userInfo['name'],userInfo['type'], userInfo['dept'], str(score))
			f.write(line + '\n')

	with open(workspace + '/output_specScore/ued得分.csv', 'w') as f:
		for item in input_javaUserInfos.items():
			id, userInfo = item
			if (userInfo['type'] != 'ued'):
				continue;			
			score = getUserSpecScore(id, uedCorrectFiles, uedAnswerFiles);
			userInfo['scoreSpec'] = score;
			line = '%s,%s,%s,%s,%s' % (id, userInfo['name'],userInfo['type'], userInfo['dept'], str(score))
			f.write(line + '\n')

	with open(workspace + '/output_specScore/dba得分.csv', 'w') as f:
		for item in input_javaUserInfos.items():
			id, userInfo = item
			if (userInfo['type'] != 'dba'):
				continue;			
			score = getUserSpecScore(id, dbaCorrectFiles, dbaAnswerFiles);
			userInfo['scoreSpec'] = score;
			line = '%s,%s,%s,%s,%s' % (id, userInfo['name'],userInfo['type'], userInfo['dept'], str(score))
			f.write(line + '\n')

	# read 主观题
	with open(workspace + '/input_otherscore/主观题分数.csv') as f:
		for line in f:
			cols = line.strip().split(',')

			if (len(cols) == 6):
				id = cols[0].lower();
				userInfo = input_javaUserInfos[id];
				if (len(cols[4]) > 0):
					userInfo['scoreZ1'] = int(cols[4]);
				if (len(cols[5]) > 0):
					userInfo['scoreZ2'] = int(cols[5]);

	with open(workspace + '/input_otherscore/java.csv') as f:
		for line in f:
			cols = line.strip().split(',')

			if (len(cols) == 3):
				id = cols[0].lower();
				question = cols[1];
				val = cols[2];
				userInfo = input_javaUserInfos[id];
				if (len(val) > 0):
					userInfo['scoreP' + question] = int(val) if val.isdigit() else val;					

	with open(workspace + '/output_specScore/得分.csv', 'w') as f:
		for id in userIdArray:
			userInfo = input_javaUserInfos[id];
			totalScore = getTotalScore(userInfo)
			line = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (id, userInfo['name'],userInfo['type'], userInfo['dept'], 
				str(userInfo['scoreSpec']), str(userInfo['scoreZ1']), str(userInfo['scoreZ2']),
				str(userInfo['scoreP1']),str(userInfo['scoreP2']),str(userInfo['scoreP3']), str(totalScore))
			print line
			f.write(line+'\n')


if __name__ == "__main__":
	if len(sys.argv) == 2:
		workspace = sys.argv[1];
	else:
		workspace = '/home/test/skill_test';
	do_work();

