# #类的相互关系
# # 依赖关系
# # 耦合性最低
# # 将一个类做的对象当参数传递给另一个对象的方法
# class Bingxiang:
# 	def __init__(self,name):
# 		self.name = name
#
# 	def open_door(self):
# 		print('开%s冰箱的门'%self.name)
#
# 	def zhuan(self, obj):
# 		print(f'将{obj.name}塞到冰箱')
#
# 	def closs_door(self):
# 		print('关%s冰箱的门'%self.name)
#
#
# class Person:
# 	def __init__(self,name):
# 		self.name = name
#
# # 将人关进冰箱分几步
# # 创建冰箱，和人
# bx = Bingxiang('美的')
# p1 = Person('赵志强')
#
# # 打开冰箱
# bx.open_door()
#
#
# # 将人塞进冰箱
# bx.zhuan(p1)
#
#
# # 关闭冰箱门
# bx.closs_door()
#
#
# # 组合关系  耦合性强
# # 将一个类的对象封装到另一个对象的属性中
#
# class Hero:
# 	def __init__(self,name,hp,atk):
# 		self.name = name
# 		self.hp = hp
# 		self.atk = atk
# 	def attack(self,obj):
# 		obj.hp -= self.atk
#
# 	def equip_weapon(self, wea):  # 装备武器
# 		self.wea = wea
# 		self.atk = self.wea.atk + self.atk  # 盖伦的攻击力变成装备加基础攻击
#
# class Weapon:
# 	def __init__(self,name,atk):
# 		self.name = name
# 		self.atk = atk
#
# 	def weapon_atk(self,obj):
# 		obj.hp -= self.atk
#
# pellow = Weapon('绣花枕头', 2)
# gailun = Hero('盖伦', 100, 10)
# hanbing = Hero('寒冰',80, 30)
#
# print(hanbing.hp)  # 显示寒冰的初始生命值80
# gailun.attack(hanbing)  # 盖伦攻击寒冰 攻击力10
# print(hanbing.hp)  # 显示被攻击后的寒冰生命值 70
# gailun.equip_weapon(pellow)  # 盖伦装备了一个绣花枕头武器 2
# print(gailun.wea.name)  # 输出盖伦的装备 绣花枕头
# gailun.attack(hanbing)  # 盖伦再次攻击寒冰 10 + 2
# print(hanbing.hp)  # 显示盖伦装备兵器后攻击寒冰后的生命值 58
#
#
# # 关联关系（两个类的关系比较紧密）
# #举例男女朋友
# # 将一个类的属性修改为另外一个类的对象
# class Boy:
# 	def __init__(self, name):
# 		self.name = name
# 		self.girl_friend = None
#
# 	def eat_dinner(self):
# 		if self.girl_friend:
# 			print('和我亲爱%s的女友一起吃晚餐' %self.girl_friend.name)
# 		else:
# 			print('吃个屎,一个人就吃泡面好了')
#
# 	def add_friend(self,obj):
# 		self.girl_friend = obj
#
# 	def break_up(self,obj):
# 		self.girl_friend = None
#
# class Girl:
# 	def __init__(self,name):
# 		self.name = name
#
# b = Boy('赵志强')
# g = Girl('陈茜')
# b.eat_dinner()
# b.add_friend(g)
# b.eat_dinner()
# b.break_up(g)
# b.eat_dinner()
# -=-=-=-=-=-=-=-=-=-=-=-=分割线-=-=-=-=-=-=-=-=-=-=-=-=-=


class Classes:  # 班级类
	def __init__(self, name,teacher=None, course=None):
		self.name = name
		self.teacher = teacher
		self.course = course
	
	def add_teacher(self, obj):	  # 关联老师
		self.teacher = obj
	
	def add_course(self, obj):  # 关联课程
		self.course = obj
	
		
class Course:
	def __init__(self, name, cycle, price):
		self.name = name
		self.cycle = cycle
		self.price = price
		
		
class Teacher:
	def __init__(self, name):
		self.name = name




class School:
	def __init__(self, name):
		self.name = name
	
	@classmethod
	def creat_classes(cls, name, cycle, price):
		obj = Classes(name, cycle, price)
		return obj
	
	
bj = Classes('高一三班')
t1 = Teacher('赵志强')
c1 = Course('python', 6, 1000)
bj.add_course(t1)
bj.add_course(c1)
s1 = School('北京')
ret = s1.creat_classes('python', 6, 10000)
print(ret.__dict__)


class A:
	@classmethod
	def f1(cls):
		print('类方法')
	@staticmethod
	def f2():
		print('静态方法')
		
	def f3(self):
		print('实例方法')
	
	@property
	def name(self):
		self.name = 'zzq'
		print(self.name)
		
	@setattr
	def name(self):
		self.name = 'xcc'
	
	@delattr
	def name(self):
		pass
	
	
a = A()
a.f1()# 实例可以调用类方法
A.f1()# 类可以调用类方法
a.f2()# 实例可以调用静态方法
A.f2()# 类可以调用静态方法

# 类方法是绑定在类上的方法，主要由类调用，会自动向类方法传递一个个参数为类本身 A.f1()  --- > A.f1(A)
print(a.f1)
print(A.f1)
#静态方法不属于绑定的方法，和函数一样的使用，无论是类还是实例都可以直接调用不会主动传递参数

print(a.f2)
print(A.f2)

# 实例的绑定方法 实例方法
a.f3()  # ----> a.f3(a) 自动向实例方法f3传递实例本身相当于 A.f3(a)
A.f3(a)  # 类也可以调用实例方法，但是必须手动传递参数，第一个参数为实例对象

# 动态属性
a.f4 # --->相当于 a.f4()
del a.name
