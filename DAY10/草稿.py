# def get_abs(n):
#     if n < 0:
#         n = int(str(n).strip("-"))
#     return n
# def add(x, y, f):
#     return f(x) + f(y)
# res = add(3, -6, get_abs)
# print(res)

# def func(a,b,c):
#     print(a+b-c)
#
# func(a=10,b=2,c=8)
# func(c=100,a=200,b=50)
# func(c=100,b=50,a=10)

# def func (a,b, c=10):
#     print(a+b+c)
# func(1,2)

# def func(a,b):
#     print(a+b)
# func(2,5)
# # 这里的值2,5是给函数func(a,b) 中的a,b 传递参数

# def func(a,b):
#     print(a+b)
# func(1,2)
# # 这里的a,b就是形参

# def func(*args,**kwargs):
# 	print(args,kwargs)
# 	# (19, 20, 'name') {'age': '28', 'game': 'lol'}
# func(19,20,'name',age='28',game='lol')

# # def func():
# #     print('我是赵志强')
# #     # return '哈哈哈哈哈'
# #     print('你是谁') # 这行代码，是不执行，前面有return
# # ret = func() # 用一个变量来接收函数的返回值
# # print (ret)
#
#
# def func():
#     print('this is func')
#
#     def func2():
#         print('this is func2')
#
#         def func3():
#             print('this is func3')
#
#         func3()
#
#     func2()
#
# func()




# def func():
#     print('this is func')
#     def func2():
#         print('this is func2')
#         def func3():
#             print('this is func3')
#         func3()
#     func2()
# func()
# 输出结果
'''
this is func
this is func2
this is func3
'''

# def get_abs(n):
#     if n < 0 :
#         n = int(str(n).strip("-"))
#     return n
# def add(x,y,f):
#     return f(x) + f(y)
# res = add(3,-6,get_abs)
# print(res)


# ret = lambda a,b : a + b
# print(ret(10,10))

'''
求100不断除以2直到商为0为止，打印每次除的商

用循环实现
'''
# n = 100
# while n != 0:
# 	n  //= 2
# 	print(n)
#
# def func(n):
# 	if n > 0:
# 		n //= 2
# 		print(n)
# 		func(n)
# func(100)
'''
用递归实现2分查找的算法，以从列表
 a = [1,3,4,6,7,8,9,11,15,17,19,21,22,25,29,33,38,69,107]
查找指定的值
'''




a = [1, 3, 4, 6, 7, 8, 9, 11, 15, 17, 19, 21, 22, 25, 29, 33, 38, 69, 107]
# 用递归二分法查找数字：
# a = [1,2,3]

# def func(n,a):
# 	x = len(a)
# 	if x > 0:
# 		if x % 2 == 0:  # 判断元素的个数是
# 			x = int(x/2)
# 		elif x % 2 == 1 :
# 			x = int((x+1)/2)
# 		try:
# 			if a[x] == n:
# 				print(f'{n}在列表中')
# 				exit()
# 			elif a[0] == n:
# 				print(f'{n}在列表的0下标')
# 			else:
# 				if n > a[x]:
# 					a = a[x+1:]
# 				elif n < a[x]:
# 					a = a[:x]
# 				func(n,a)
# 		except IndexError:
# 			print(f'元素{n}不存在列表中....')
# func(38,a)





def wrapper(index):
	def inter():
		print('交门票看美女')
		index()
	return inter

# @wrapper
# def func():
# 	print('冒险岛欢迎你...')
# @wrapper
@wrapper
def func2():
	print('北京欢迎你!')


func2()
# func()