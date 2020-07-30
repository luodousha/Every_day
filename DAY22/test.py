# import os
# import shutil
# 1、对文件内容的增删改查
# 新增文件夹或者文件
# print(__file__)  # 当前文件运行路径
# BASE_DIR = os.path.dirname(__file__)  # 相当于os.getcwd()
# print(BASE_DIR)
# 增 文件夹
# 在当前文件夹下创建单一文件
# os.mkdir('gg')
# with open('gg/__init__.py', 'w') as f:
# 	pass
# os.makedirs('a/b/a/c/d/e')


# 删除# 删除单一空文件,必须要删掉文件中的内容才可以删掉文件夹
# lis=os.listdir('gg')
# print(lis)
# file = BASE_DIR+'/'+'gg'+'/'+lis[0]
# os.remove(file)
# os.rmdir('gg')
# os.removedirs('gg')  # 假如文件不为空就会报错


# 递归删除文件
# os.removedirs('a')
# lis = os.listdir(os.getcwd())
# print(lis)
# l = os.getcwd()  # 返回当前文件路径
# print(l)
# os.removedirs('a')
# os.makedirs('a/b/c/d/e')  # 创建多层级空文件夹
# file_path = BASE_DIR+'/'+'a/b/c/d/e'
# print(file_path)
# shutil.rmtree('a')  # 删除文件夹下所有的文件
# os.removedirs(file_path) # 若子文件子文件为空就会尝试删除父文件父文件也为空也会删除

# 改文件，文件名更改,移动文件
# os.mkdir('gg')
#1 重命名
# os.rename('gg', 'game_over')
#2 移动文件
# os.rename('gg', 'game_over/gg')


# 查文件，有没有文件
# 查看当前文件夹下内容
# print(os.getcwd())  #返回当前的文件夹
# print(os.listdir(os.getcwd()))
# 以列表的形式返回当前文件下的文件或文件
# ['game_over', 'test.py', '考核二']


# 返回文件的绝对路径
# os.path.abspash('path')
# 返回当前的绝对路径
# print(os.path.abspath('.'))
# 返回文件game_over的绝对路径
# print(os.path.abspath('game_over'))


# 判断文件是是否是文件夹
# os.path.isdir()
#  判断给定的path是不是文件夹
# print(os.path.isdir('game_over'))

#  判断给定的path是不是文件
# print(os.path.isfile('game_over'))



# 2、函数 参数的形式及其区别
# def func(a,b): # a, b就是形参
# 	print(a+b)


# 函数的参数有实参，形参
#实参：给函数传递的值
#形参：函数接收的值

#实参
# 按照传递方式区别：
# 位置传参 按照位置传递
# 关键字传参（关键字传参位置要在位置参数的后面）

# func(1,2) # 1,2 就是实参，传递方式是按照位置传递 a接收1 , b接收2
# func(a=1,b=5) # 传递方式是 关键字传参，
# func(b=19,a=34)

# 为了避免形参接收参数混乱关键字传参位置必须在位置参数后面
# func(3, b=10)  # 可以
# func(3,a=10) # 不可以 形参接收的分不清第一个值是给a,还是给b

# 形参
# 按照位置接收实参
# func(1, 3)  #函数func按照位置第一个形参a接收实参1

# 默认值参数
# def fun(a,b=10):
# 	print(a-b)
# fun(3)
# fun(10, 99)
# 不定长接收参数
# *args , **kwargs
# args 以元组形式接收
# kwargs 以字典形式接收
# def func(a,b,*args,**kwargs):
# 	print(a, b)
# 	print(args,kwargs)
# func(1,2,4,4,5,10, name='zzq', age=29)
# func(4,4,5,10,11, name='zzq', age=29)


# 3、装饰器及其应用、闭包及其应用
#开发原则
# 开闭原则
# 对扩展开发对修改关闭
#装饰器
#应用 假如需要拓展新功能，要求1不修改源代码，要求2不改变函数调用方式

# 例如有需求给函数index添加一个功能
# 先登录的功能

def wrapper(func):
	def inter(*args,**kwargs):
		if login():
			func(*args, **kwargs)
	return inter
# index = wrapper()


def login():
	user_in  = input('请输入用户名:')
	user_pass = input('请输入密码:')
	if user_in == 'zzq' and user_pass == '123':
		print('登录成功')
		return True
	else:
		return False


@wrapper  # 语法糖 相当于index = wrapper(index)
def index(num,**kwargs):
	print('欢迎进入index页面')
	print(num)
	print(kwargs)
# index = wrapper()

# index(5,name='zzq')





# 4、作用域
#LEGB

# 5、迭代器，生成器，可迭代对象
#1:iterable 可迭代对象对象本身有__iter__（）方法
#2: 迭代器本身有__iter__方法和__next__
# 迭代器是迭代对象
#3:  generator 生成器
# 生成器特点 惰性机制只调用的时候才能成数据，只能用一次

# 6、递归函数 在函数内部调用自身的函数

# 7、匿名函数 lambda

# 8、内置方法考察 zip filter map。。。。
# zip(可迭代对象)
#返回一个zip对象
k = [1,2,3,4]
v = [4,5,6,7]
z=zip(k)
print(list(z))
for i in z:
	print(i)
#可以通过* 解压
# a,b= zip(k,v)




# 9、模块 time re json
