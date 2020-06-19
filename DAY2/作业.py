'''
查一下如何，打印颜色....
'''
'''
\033[显示方式;前景色；背景色m需要显示的文字\033[0m
1、显示方式：
0（默认）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
2、前景色：
30（黑色）、31（红色）、32（绿色）、 33（×××）、34（蓝色）、35（洋 红）、36（青色）、37（白色）
3、背景色:
40（黑色）、41（红色）、42（绿色）、 43（×××）、44（蓝色）、45（洋 红）、46（青色）、47（白色）
'''
# print('\033[1;32;32m game over \033[0m')

# 7 写代码
'''
[1]
实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,
显示登陆成功,否则登陆失败!
'''
# user_name = input('请输入用户名：')
# user_pass = input('请输入密码：')
# if user_name == 'seven' and user_pass == '123':
# 	print('登录成功')
# else:
# 	print('登录失败')
'''
[2]
实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,
显示登陆成功,否则登陆失败,失败时允许重复输入三次
'''
# count =3
# while count !=0:
# 	print(f'你还有{count}机会')
# 	user_name = input('请输入用户名：')
# 	user_pass = input('请输入密码：')
# 	if user_name == 'seven' and user_pass == '123':
# 		print('登录成功')
# 		break
# 	else:
# 		print('登录失败')
# 	count-=1

'''
[3]
实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为
123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
'''
# count =3
# while count !=0:
# 	print(f'你还有{count}机会')
# 	user_name = input('请输入用户名：')
# 	user_pass = input('请输入密码：')
# 	if(user_name == 'seven' or user_name == 'alex') and user_pass == '123':
# 		print('登录成功')
# 		break
# 	else:
# 		print('登录失败')
# 	count-=1

'''
8 写代码
	使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12
	
	使用while 循环输出100-50，从大到小，如100，99，98…，到50时再从0循环输出到50，然后结束
	
	使用 while 循环实现输出 1-100 内的所有奇数
	
	使用 while 循环实现输出 1-100 内的所有偶数
	
	使用while循环实现输出2-3+4-5+6…+100 的和
'''
# 8.1
# i = 0
# while i < 12:
# 	i += 1
# 	if i == 6:
# 		continue
# 	elif i == 10:
# 		continue
# 	else:
# 		print(i)
#
# 8.2
# n  =  100
# while n > 0:
# 	print(n)
# 	n -= 1
# 	if n == 50:
# 		n=0
# 		while n <= 50:
# 			print(n)
# 			n += 1
# 		break

# 8.3
# n = 1
# while  n < 100:
# 	print(n)
# 	n += 2

#8.4
# n = 2
# while n < 101 :
# 	print(n)
# 	n += 2

# n = 2
# sum = 0
# while  n < 101:
# 	if n % 2 == 0:
# 		sum += n
# 	else:
# 		sum -= n
# 	n+=1
# print(sum)

'''
9 现有如下两个变量,请根据执行结果解释原因
n1 = 123456
n2 = n1
n1 = 333
# print(n1,n2)
# '''
# n1 = 123456
# # print(id(n1))
# n2 = n1
# # print(id(n2))
# n1 = 333
# # print(id(n1))
# print(n1, n2)
'''
n1 先是指向 123456 字符串地址
接着 n2 也同样指向 123456 的内存地址
然后n1 被赋值 指向了新的内存地址为 333 的内存地址
打印的时候就输出了n1指向内存地址的值 为333 n2指向内存地址的值为123456
'''

'''
10 制作趣味模板程序（编程题）

    需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意显示

    如：敬爱可爱的xxx，最喜欢在xxx地方干xxx
'''
# name = input('请输入人名：')
# adress = input('请输入地点：')
# hobbie = input('请输入爱好：')
# msg = f'''
# 敬爱可爱的{name},最喜欢在{adress}地方干{hobbie}
# 	'''
# print(msg)

# 11
'''
11 输入一年份，判断该年份是否是闰年并输出结果。（编程题）

    注：凡符合下面两个条件之一的年份是闰年。
   （1） 能被4整除但不能被100整除。 （2） 能被400整除。
'''
# year = int(input('请输入年份：'))
# if year % 4 == 0 and not year % 100 == 0:
# 	print(f'{year},是闰年')
# elif year % 400 == 0  :
# 	print(f'{year},是闰年')
# else:
# 	print(f'{year}不是闰年')


'''
12假设一年期定期利率为3.25%，
计算一下需要过多少年，一万元的一年定期存款连本带息能翻番？
'''
# n = 0.00325
# money = 10000
# year = 0
# while money <= 20000:
# 	money  *= 1 + n
# 	year += 1
# print(str(year))

# 13
'''
3 使用while,完成以下图形的输出
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
'''
# n = 1
# while  n <= 9 :
# 	print( n * '*')
# 	while n >= 5 and n < 9 :
# 		print('*'*(9-n))
# 		n += 1
# 	n += 1

# count = 0
# while count < 10 :
# 	count += 1
#
# 	if count <= 5 :
# 		print(count * ' * ')
# 	elif count < 10 :
# 		print((10 -count) * ' * ' )

'''
14
    一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
    求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
# height = 100
# times = 0
# total = 0
#
# height = 100
# times = 0
# total = 0
#
# while times < 10 :
# 	times += 1 # 经过的掉落时间
# 	new_height =  height/2
# 	total = 2* new_height # 本次经过的距离
#
# 	height = new_height # 高度被重置
#
# print(times,height,100+total)