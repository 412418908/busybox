#!/bin/env python -u

import sys
import re

# python join.py file1.csv:a1,a2 file2.csv:b1 'a1(b2,b3),a2(b2,b3),b2,a3'

if len(sys.argv) != 4:
	print 'usage: python join.py file1.csv:a1 file2.csv:b1 \'a1(b2;b3),a2,a3\''
	exit(0);	


file1 = sys.argv[1]
file2 = sys.argv[2]
output = sys.argv[3]

file1_name = file1.split(':')[0]
file1_col = int(file1.split(':')[1][1:]) - 1
file2_name = file2.split(':')[0]
file2_col = int(file2.split(':')[1][1:]) - 1

file2_map = {}; # key: cols[b1],  value: [b1,b2,b3,..]
with open(file2_name,'r') as file:
	for line in file:
		cols = line.strip().split(',')
		if len(cols) < 1:
			continue;
		key = cols[file2_col]
		file2_map[key] = cols;

# parse output format



fmt = re.compile(r'[ab]\d+')
var_names = fmt.findall(output)  #['a1', 'b2', 'b3', 'a2', 'a3']
outputfmt,number = fmt.subn('%s', output)


#print 'file2_map=', file2_map
with open(file1_name, 'r') as file:
	for line in file:
		cols = line.strip().split(',')
		if len(cols) <= 1:
			print line
			continue;
		key = cols[file1_col]
		file2_vals = file2_map[key]
		file1_vals = cols;
		# output formated vals
		vars = ()
		for name in var_names:
			idx = int(name[1:])-1
			if name.startswith('a'):
				vars = vars + (file1_vals[idx],);
			if name.startswith('b'):
				vars = vars + (file2_vals[idx],);
		print outputfmt%vars

    



