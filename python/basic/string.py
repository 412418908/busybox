1.字符串属性方法操作:

1.>字符串格式输出对齐

1
2
3
4
5
6
7
8
9
10
11
>>> str = "Python stRING" 
 
>>> print str.center(20)       #生成20个字符长度，str排中间
   Python stRING   
    
>>> print str.ljust(20)            #生成20个字符长度，str左对齐
Python stRING      
 
>>> print str.rjust(20)            #生成20个字符长度，str右对齐
       Python stRING
       
2.>大小写转换

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
>>> str = "Python stRING"
 
>>> str.upper()                #转大写
'PYTHON STRING'
 
>>> str.lower()                #转小写 
'python string'
 
>>> str.capitalize()       　　　　#字符串首为大写，其余小写
'Python string'
 
>>> str.swapcase()         #大小写对换 
'pYTHON STring'
 
>>> str.title()                #以分隔符为标记，首字符为大写，其余为小写
'Python String'
3.>字符串条件判断

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
>>> str = '01234'
 
>>> str.isalnum()                #是否全是字母和数字，并至少有一个字符
True
>>> str.isdigit()                #是否全是数字，并至少有一个字符
True      
 
 
>>> str = 'string'
 
>>> str.isalnum()                  #是否全是字母和数字，并至少有一个字符
True
>>> str.isalpha()                  #是否全是字母，并至少有一个字符 
True
>>> str.islower()                  #是否全是小写，当全是小写和数字一起时候，也判断为True
True
 
>>> str = "01234abcd"
 
>>> str.islower()                  #是否全是小写，当全是小写和数字一起时候，也判断为True
True
 
>>> str.isalnum()                  #是否全是字母和数字，并至少有一个字符
True
 
>>> str = ' '
>>> str.isspace()                  #是否全是空白字符，并至少有一个字符
True
 
>>> str = 'ABC'
 
>>> str.isupper()                  #是否全是大写，当全是大写和数字一起时候，也判断为True
True
 
>>> str = 'Aaa Bbb'
 
>>> str.istitle()                  #所有单词字首都是大写，标题 
True
 
 
>>> str = 'string learn'
 
>>> str.startswith('str')   　　　　　　　　　　　　　　#判断字符串以'str'开头
True
 
>>> str.endswith('arn')        　　　　　　　　　　　　　　#判读字符串以'arn'结尾
True
4.>字符串搜索定位与替换

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
>>> str='string lEARn'
 
>>> str.find('z')              #查找字符串，没有则返回-1，有则返回查到到第一个匹配的索引
-1
 
>>> str.find('n')              #返回查到到第一个匹配的索引
4
 
>>> str.rfind('n')         #返回的索引是最后一次匹配的
11
 
>>> str.index('a')         #如果没有匹配则报错 
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: substring not found
  
>>> str.index("n")      #同find类似,返回第一次匹配的索引值
4
 
>>> str.rindex("n")         #返回最后一次匹配的索引值
11
 
>>> str.count('a')      #字符串中匹配的次数
0
>>> str.count('n')      #同上
2
 
>>> str.replace('EAR','ear')        #匹配替换
'string learn'
 
>>> str.replace('n','N')
'striNg lEARN'
 
>>> str.replace('n','N',1)
'striNg lEARn'
 
>>> str.strip('n')          #删除字符串首尾匹配的字符，通常用于默认删除回车符 
   
'string lEAR' 
   
>>> str.lstrip('n')        #左匹配 
   
'string lEARn' 
   
>>> str.rstrip('n')        #右匹配 
   
'string lEAR' 
 
>>> str = " tab"
 
>>> str.expandtabs()       #把制表符转为空格
' tab'
 
>>> str.expandtabs(2)      #指定空格数
' tab'
5.>字符串编码与解码

1
2
3
4
5
6
7
8
9
10
11
12
>>> str = "字符串学习"
>>> str
'\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2\xe5\xad\xa6\xe4\xb9\xa0'
 
>>> str.decode('utf-8')                                #解码过程，将utf-8解码为unicode
u'\u5b57\u7b26\u4e32\u5b66\u4e60'
 
>>> str.decode("utf-8").encode('gbk')                      #编码过程，将unicode编码为gbk
'\xd7\xd6\xb7\xfb\xb4\xae\xd1\xa7\xcf\xb0'
 
>>> str.decode('utf-8').encode('utf-8')                        #将unicode编码为utf-8 
'\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2\xe5\xad\xa6\xe4\xb9\xa0'
6.>字符串分割变换

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
>> str = "Learn string"
 
>>> '-'.join(str)
'L-e-a-r-n- -s-t-r-i-n-g'
 
>>> li = ['Learn','string']
 
>>> '-'.join(li)
'Learn-string'
 
>>> str.split('n')
['Lear', ' stri', 'g']
 
>>> str.split('n',1)
['Lear', ' string']
 
>>> str.rsplit('n')
['Lear', ' stri', 'g']
 
>>> str.rsplit('n',1)
['Learn stri', 'g']
 
>>> str.splitlines()
['Learn string']
 
>>> str.partition('n')
('Lear', 'n', ' string')
 
>>> str.rpartition('n')
('Learn stri', 'n', 'g')