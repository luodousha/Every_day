# 操作类中有没有此字符串的属性
class A:
	country = '中国'
	def func(self):
		print('from A.func ')
	def __init__(self,name):
		self.name
#查找对象属性，返回布尔值
#hasattr()
print(hasattr(A,'func'))
print(hasattr(A,'sjdks')) # 找不到不会报错，只会返回False
#获取对象属性
#getattr(对象，str,返回值（默认是None）)
if getattr(A,'func'):
	print('有这个方法...')
# setattr() 设置属性，修改
setattr(A,'country','美国') # 修改属性
setattr(A,'name','zzq')
print(A.name) # 是类属性
print(A.country)
print(A.__dict__)
# delattr(A,'name') # 删除属性
# print(A.__dict__)


# 当对象是实例对象的时候
a = A('lw')
setattr(a,'name','xcc')
print(a.name)
# 反射的对象可以是类，也可以是实例对象
ret = getattr(a,'name')
print(ret)
print(a.__dict__)
