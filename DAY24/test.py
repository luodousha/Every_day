# 从文件中读出以个pickle数据 转换为我需要的数据我需要的数据
import pickle

class Admin:
	def __init__(self, name):
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

