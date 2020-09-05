#  创建一个学生类
# class Student:
# 	country = 'CHINA'  # 类属性
# 	def func(cls):  #类方法
# 		print('这是类方法...')
#
# 	def __init__(self,name,age,gender): # 构造方法 每次实例化对象就会调用此方法
# 		self.Name = name
# 		self.Age = age
# 		self.Gender = gender
#
#
# 	def eat(self):
# 		print(f'{self.Name}很会吃')
#
# 	def sleep(self):
# 		pass
#
# 	# def __del__(self):
#
# stu1  = Student('zzq',19,'male')
# print(stu1.__dict__) #这里输出的字典是实例对象，实例属性
# print(Student.__dict__)
# stu2 = Student('xcc',20,'female')
# stu2 = Student('lw',27,'male')
# # del stu1
# # 所谓类属性，类方法是共用一个内存地址，这里要注意
# print(stu1.country,id(stu1.country))
# print(stu2.country,id(stu1.country))
# Student.country = []
# print(stu2.country)
# stu2.country.append(1)
# print(stu1.country)  # 类属性，类方法是实例对象共用，指向的内存地址是相同的


'''
练习1 编写一个学生类，创建一系列学生
要求： 要有一个属性，统计创建多少个实例对象
'''

# class Student():
# 	count = 0
# 	def __init__(self,name,age,gender):
# 		self.name = name
# 		self.age = age
# 		self.gender = gender
# 		Student.count += 1
#
#
# stu1  = Student('zzq',19,'male')
# stu2 = Student('xcc',20,'female')
# stu2 = Student('lw',27,'male')
# print(stu1.count)


# class Hero:
# 	def __init__(self,name,attack,hp):
# 		self.name = name
# 		self.attack = attack
# 		self.hp = hp
#
# 	def attack_hero(self, obj):
# 		# print(f'{self.name}发起了攻击')
# 		print(f'{self.name}攻击了{obj.name}')
# 		if obj.hp > 0:
# 			obj.hp -= self.attack
# 		else:
# 			print(obj.hp)
# 			print(f'{obj.name}已经被打死')
#
# 	def diss_hp(self):
# 		print(f'{self.hp}')
#
#
#
# gai = Hero('盖伦', 10, 100)
# han = Hero('寒冰', 15, 90)

# # gai.attack_hero(han)
# han.attack_hero(gai)
# # print(gai.hp,han.hp)
# han.attack_hero(gai)
# han.attack_hero(gai)
# han.attack_hero(gai)
# han.attack_hero(gai)
# han.attack_hero(gai)
# han.attack_hero(gai)
# han.diss_hp()
# gai.diss_hp()

class Persion:
	school = '路飞学院'
	def __init__(self,name,age,gender):
		self.name = name
		self.age = age
		self.gende = gender
	
	
class Teacher(Persion):
	def __init__(self, course):
		super().__init__()
		self.course = course
	

t1 = Teacher('Python','zzq',28,'male')