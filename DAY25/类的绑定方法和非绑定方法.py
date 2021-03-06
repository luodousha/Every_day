# 类里的方法分为绑定方法和非绑定方法

# 绑定方法
# 绑定到类主要由类进行调用，方法第一个参数默认传递类（类方法）
# 绑定到实例主要由实例对象调用，方法默认第一个参数传递对象本身（实例方法）

# 非绑定方法，不会默认传递参数，与函数类似

class A:
	@classmethod
	def f1(cls):
		print('绑定方法之类方法')
	def f2(self):
		print('绑定方法之实例方法')
	
	@staticmethod
	def f3():
		print('没有被绑定,与函数是一样之静态方法')
	
# 举例什么时候采用
