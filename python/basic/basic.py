
#!/usr/bin/python
# -*- coding: UTF-8 -*-

print  '你好世界'

name = "madisetti"  # 注释

'''
多行注释

'''


# 等待用户输入 

raw_input("enter to exit.\n");


# print 不换行 

x = "a"
y = "b"
print x, y
print x,
print y,
print "###"


#-------------------------文件操作
import os
os.listdir('/root')
os.mkdir('/root/tmp2', 0666)


#-------------------------读取文件
with open('/root/100.nb', 'r') as f:
	line = f.readline()
	while line:
		print line
		line = f.readline()

with open('/root/100.nb', 'r') as file :
	for line in file:
		print line
		

#-------------------------------字符串
 
 # 去除前后空格 
 s = "hello  ";
 s = s.strip()
 #字符串长度
 len(s)

s = r'e:\work\path' # 不进行字符串转义

#字符串分割为数组
s = "name,age,address"
cols = s.split(',')
print cols[0], cols[1], cols[2]

#----------------------------------list, 数组类型 
list = ['hello'];
list.append('world')
list[1];  #world
list[0:]; #hello world 

list.append('java')
len(list)
list.index('world') #1
list.inser(2, 'python')
list.pop();
list.remove('java')

