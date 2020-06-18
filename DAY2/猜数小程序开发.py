# _*_ coding:utf-8 _*_

# import random
# print('猜数字v1.0测试版')
# n = random.randint(0,10)# 从[0-10]中随机电脑选择一个数，给用户猜测
#
# user_guess = int(input('请输入你猜的数字：'))
#
# if user_guess > n :
# 	print('猜大了，再试试...')
# elif user_guess < n :
# 	print('猜小了，再试试...')
# else:
# 	print('恭喜你成功猜对数字%s'%n)
# print('数字是%s'%n)

# 猜数字怎么只能猜一次呢？要多次猜测记录并记录猜了几次
# import random
# print('猜数字小游戏v2.0版')
# count = 0
# num = random.randint(0,10)# 从[0-10]中随机取一个数字

# while True:
# 	count += 1
# 	user_guess = input('请输入你要猜的数字（按q/Q退出程序）：')
# 	if user_guess.strip().upper() =='Q':
# 		exit()
# 	else:
# 		user_guess= int(user_guess)
#
# 	if user_guess > num :
# 		print('你猜大了,再试试')
#
# 	elif user_guess < num :
# 		print('你猜小了，再试试')
#
# 	else:
# 		print(f'恭喜你猜对了... 你猜了{count}次')

'''
练习2：猜数字升级版 (10分钟)
要求：
允许用户最多尝试3次
每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
如何猜对了，就直接退出

'''
import random
 # 随机电脑取一个数字
num = random.randint(0, 10)
count = 3
print('猜数小程序3.0')
while True:
	user = input('是否继续y/n')
	count = 3
	if user.upper() == 'Y':
		while count != 0 :
			print(f'你还有{count}次机会')
			user_in = int(input('请输出猜测的数字：'))
			if user_in >num :
				print('猜大了，往小了试试')
			elif user_in <num :
				print('猜小了，往大了试试')
			else:
				print('恭喜你猜对了....')
				exit()
			count -=1
	else:
		exit()