class Student:
	def __init__(self, name, age):
		self.__name = name
		self.__age = age
	@property  # 加了这个property 装饰器后s.name就相当于s.name()
	def name(self):
		print(self.__name)
		# pass
	
	@name.setter  # 设置属性
	def name(self,new):
		if not isinstance(new,str):
			print('属性必须是字符串类型')
			return
		self.__name = new
	
	@name.deleter  # 删除属性
	def name(self):
		del self.__name
	
	@property
	def age(self):
		print(self.__age)
	
	@age.setter
	def age(self, new_age):
		if not isinstance(new_age, int):
			print('年龄属性必须是数字整形...')
			return
		self.__age = new_age
		
	def func(self):
		print('from A func')

s1 = Student('zzq',10)
s1.name
s1.name = 1
s1.name
# del s1.name
# print(s1.__dict__)
# print(Student.__dict__)
# s1.age = 10
s1.age
# s1.age = 'a'
s1.age = 28
s1.age