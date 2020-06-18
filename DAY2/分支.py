#单分支：
name = '赵志强'

if name=='赵志强':
	print('老单身狗%s'%name)

#双分支：

girl_friend = ''
if girl_friend:
	print('恭喜啊，居然有女朋友了')
else:
	print('求求你快恋爱吧.%s.'%name)

#多分支：
'''
判断成绩档次小程序
90-100 A
80-89  B
60-79  C
40-59  D
0 -39  E
程序启动，用户输入成绩，根据成绩打印等级
'''
score = int(input('请输入你的成绩：'))

if 90<= score <= 100:
	print('A')
elif 79<score<90:
	print('B')
elif 59<score<80:
	print('C')
elif 39<score<60:
	print('D')
elif 0<=score <40 :
	print('E')
else:
	print('输入错误，请重试')
	