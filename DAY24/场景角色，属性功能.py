import sys
import pickle
print(sys.modules[__name__])
class Student:
	'''
	学生
	'''
	def __init__(self,name,age ,classes= None):
		self.name = name
		self.age = age
		self.classes = classes  # 关联班级
		self.course_list = []
	
	def select_courses(self):
		print('选课')
		
	def select_classes(self):
		print('选择班级')
	
	def check_course(self):
		print('查看所选课程')
		for i in self.course_list:
			print(i,end='')
			
	def pay_tuition(self):
		print('交学费')
		
	def register(self):
		print('注册')


class Admin:
	def __init__(self,name):
		self.name = name
		
	def create_course(self):
		print('创建课程')
	
	def create_teachers(self):
		print('创建讲师')
		
	def create_students(self):
		print('创建学生')
		
	def create_classes(self):
		print('创建班级')
		
	def exit(self):
		print('退出,欢迎再次使用...')
		exit()
	

def login():
	user_in = input('username:')
	user_pwd = input('password:')
	if not user_in:
		print('不允许输入空值')
		exit()
	with open('user_info', 'r', encoding='utf-8') as f:
		for line in f:
			name, pwd, identify = line.strip().split(',')
			if name == user_in and pwd == user_pwd:
				print('登录成功')
				obj = Admin(name)
				return {'name': name, 'identify': identify, 'result': True}
			else:
				print('登录失败，用户名或密码错误')
				return {'name': None, 'identify': None, 'result':False}


# dic = {'name':'lw','idendify':'teacher'}
