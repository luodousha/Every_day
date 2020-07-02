##1写函数，计算传入数字参数的和。（动态传参）
# def func(*args,**kwargs):
# 	return sum(args)
# ret=func(2,3,4,5,6,6,7)
# print(ret)

'''
写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
'''


def func(file_name, old_str, new_str):
	import os
	try:
		with open(file_name, 'r', encoding='utf-8')as f:
			str = f.read().strip()
		with open('aa.txt_new', 'w', encoding='utf-8') as f2:
			# print(str)
			if old_str in str:
				str = str.replace(old_str, new_str)
				f2.write(str)
	except Exception as e:
		print(e)
	os.replace('aa.txt_new', 'aa.txt')


# func('aa.txt','s','ss')

'''
写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有' '内容。
'''


def func(x):
	count = 0
	for i in x:
		if i == ' ':
			count += 1
	print(f'有空格{count}个')


# func(' a b b b bb ')


# 第四题
'''
写函数，检查传入字典的每一个value的长度,如果大于2，
那么仅保留前两个长度的内容（对value的值进行截断），
并将新内容返回给调用者，注意传入的数据可以是字符、list、dict
'''
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# def func(dic):
# 	for k, v in dic.items():
# 		if len(v)> 2:
# 			dic[k] = v[:2]
# 		else:
# 			continue
# 	return dic
# ret = func(dic)
# print(ret)
# 题5
'''
写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
[(‘红心’，2),(‘草花’，2), …(‘黑桃A’)]
'''
# def func():
# 	lis3 = []
# 	lis = [x for x in range(2,11)]
# 	lis.extend(['A','J','Q','K'])
# 	lis2 = ['红桃','黑桃','方块','梅花']
# 	for i in lis:
# 		for j in lis2:
# 			lis3.append((j,i))
# 	return lis3
# print(func(),len(f))
# 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# def func(*args):
# 	dic = {}
# 	try:
# 		for i in args:
# 			if type(i) is int or float:
# 				dic['max'] = max(args)
# 				dic['min'] = min(args)
# 		return dic
# 	except TypeError:
# 		# print('只支持数字类型')
# 		return '类型错误'
# print(func(1,2,3,4.5,5,7,7,8,9.4))

# 写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 例如:min_max(2,5,7,8,4)
# 返回:{‘max’:8,’min’:2}
# def func(t):
# 	max_= t[0]
# 	min_= t[0]
# 	for i in t:
# 		if max_<i:
# 			max_ = i
# 		min_ =min_ if i>min_ else i
# 	dic = dict(max=max_,min = min_)
# 	return dic
# print(func((10,5,78,4)))

'''
写函数，专门计算图形的面积
其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积

调用函数area(‘圆形’,圆半径) 返回圆的面积
调用函数area(‘正方形’,边长) 返回正方形的面积
调用函数area(‘长方形’,长，宽) 返回长方形的面积
'''
# import math
# def func(name,*args):
# 	print('''
# 请按照以下格式输入
# 调用函数area(‘圆形’,圆半径) 返回圆的面积
# 调用函数area(‘正方形’,边长) 返回正方形的面积
# 调用函数area(‘长方形’,长，宽) 返回长方形的面积''')
# 	def area_c(*args):
# 		area = args[0]*args[1]
# 		return name,area
# 	def area_z(*args):
# 		# print(args)
# 		area = args[0]**2
# 		return name,area
# 	def area_y(*args):
# 		area = math.pi * args[0] ** 2
# 		return name,area
# 	if name == '圆形':
# 		return area_y(*args)
# 	elif name == '长方形':
# 		return area_c(*args)
# 	elif name == '正方形':
# 		return area_z(*args)
# 	else:
# 		return '请输入正确的图形名字'
# print(func('正方形',5))
# print(func('长方形',3,4))


'''
写一个函数返回他的阶乘
'''


# 用循环解决
# def func(n):
# 	ret = 1
# 	for i in range(n,0,-1):
# 		ret = ret*i
# 	return ret
# print(func(7))
# 用递归解决
def func(n):
	ret = 1
	if n == 1:
		return ret
	else:
		ret = n * ret
		n -= 1
		return ret * func(n)


print(func(7))

'''
编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）user_info.txt
要求登录成功一次，后续的函数都无需再输入用户名和密码
'''

# 读取文件
def func():
	dic = {}
	with open('user_info.txt', 'r', encoding='utf-8') as f:
		for line in f:
			line = line.strip()
			user_n = line.split(',')[0]
			user_p = line.split(',')[1]
			dic[user_n] = user_p
	return dic


#装饰器函数，增加登录功能
def wrapper(index):
	def inter(*args, **kwargs):
		file_dic = func()
		user_in = input('请输入用户名')
		user_pd = input('请输入密码')
		if user_in in file_dic and file_dic[user_in] == user_pd:
			print('登录成功')
			file_dic['register']='Ture'
			index(*args,**kwargs)
			
		else:
			print('用户名或密码错误...')
	return inter

@wrapper
def home():
	print('欢迎进入主页')

@wrapper
def japan():
	print('欢迎进入日本专区')

@wrapper
def western():
	print('欢迎进入欧美专区')

home()