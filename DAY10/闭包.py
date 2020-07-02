'''
闭包作用
1 保护变量 # 外部不能修改，访问，变量不能被修改，很安全
2 常驻内存
'''

# def outer():
# 	name = '赵志强' # 定义局部变量
# 	def inter():
# 		print(name)  # 在内层函数中使用
# 	return inter  # 返回内层函数的内存地址
#
# ret=outer()
# ret()

# 装饰器
# 在要求不改变函数调用方式，不修改源代码的基础上，需要对函数进行扩展
#  这就需要用装饰器对函数进行扩展
# 例如有一个函数是func认证
# 现在有新需求在他的前面加一句欢迎，不修改代码，不修改调用方式，如何实现？？
# def outer(func): # 定义一个装饰函数，将原函数内存地址传入
# 	def inter(): # 定义一个内置函数
# 		print('欢迎') # 扩展新的功能
# 		func()  # 原函数
# 	return inter  #  返回内层函数地址

# @outer # 这是python的语法糖，本质是闭包的应用
# def func():
# 	print('认证....')
# 原调用方式
# func()
# 装饰器也是闭包的一种应用
# # func = outer(func)  # 对原函数进行赋值，使调用方式不发改变
# # func()


# def outer(func):
# 	age = input('你有多大了')
# 	def inter(*args,**kwargs):
# 		print(f'{age}了要结婚了')
# 		func(*args,**kwargs)
# 	return inter
# @outer
# def func(name,hobbie):
# 	print('我是谁？')
# 	print(f'{name},喜欢{hobbie}')
# # func = outer(func)
# # func()
# func('赵志强','篮球')



# 列表a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],要求你把列表里的每个值加1
a = [x  for x in range(10)]
print(a)




# map()版本
def func(x):
	return x+1
a2 = map(func,a)
print(list(a2))

# 列表推导式
a3 = [x for x in range(1,11)]
print(a3)

a4 = [x+1 for x in range(10)]
print(a4)

lis1 = ['zzq','pwk']
lis2 = ['赵志强','潘吾可']
dic = {x:y for x ,y in zip(lis1,lis2)}
print(dic)
# 输出结果{'zzq':'赵志强','pwk':'潘吾可'}

#列表推导式：
# lis1=[x for x in range(10000)]
# #生成器推导式：
# lis2 = (x for x in range(10000))
# print(lis1)
# print(lis2)
'''
著名的斐波拉契数列（Fibonacci），
除第一个和第二个数外，任意一个数都可由前两个数相加得到：

1, 1, 2, 3, 5, 8, 13, 21, 34, …
'''

def func(max):
	n = 1
	s = 0
	lis = []
	while s < max:
		if n == 1 or n == 2:
			lis.append(1)
		else:
			s = sum(lis[-2:])
			lis.append(s)
		n += 1
	for i in lis:
		# print(i)
		yield i
	# return lis
# ret=func(100)
# print(ret)
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())
# print('我想去拉屎')
# print(ret.__next__())
# print(ret.__next__())
# print(ret.__next__())









