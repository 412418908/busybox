

##

python skill_test.py  workfolder(D:/github/busybox/python/usecase/考试改卷)

输入：
  input_userinfo目录
     名单.csv
     格式：  工号,姓名,类型,部门
  input_spec目录
     
     java/correct/*.txt
     java/answer/*.txt
     dba/correct/*.txt
     dba/answer/*.txt
     ued/correct/*.txt
     ued/answer/*.txt
     格式： [第i题]: A/B/C/D

  input_otherscore:
     主观题分数.csv 格式： 工号,姓名,类型，部门，分1，分2
     java.csv 格式： 工号,题号,分

输出:
  output_specScore目录
     java得分.csv   格式： 工号,姓名,类型,部门,分数
     dba得分.csv    格式： 工号,姓名,类型,部门,分数
     ued得分.csv    格式： 工号,姓名,类型,部门,分数
    
    得分.csv   格式：工号,姓名,类型,部门,编程规范得分,主观1，主观2，编1，遍2，遍3,总分
  
    
