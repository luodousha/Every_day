# 需求
"""
1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课通程包含，周期，价格，过学校创建课程
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级
5. 创建讲师角色时关要联学校
6. 提供三个角色接口
    6.1 学员视图， 可以注册， 交学费， 选择班级
    6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
    6.3 管理视图，创建讲师， 创建班级，创建课程
7. 上面的操作产生的数据都通过pickle序列化保存到文件里
"""
import pickle


class School:  # 学校类
	admin_lis = []
	def __init__(self, name, site):
		self.name = name
		self.site = site
	
	def create_course(self,course_name,course_cycle,course_price):
		course = Course(course_name,course_cycle, course_price)
		return course
	def create_classes(self, class_name, course):
		'''
		创建班级
		:return:
		'''
		pass
	
	@staticmethod
	def mandate(obj):  # 给某些人权限，用来创建班级，创建讲师，创建课程
		School.admin_lis.append(obj.name)
		
	
class Course:  # 课程类(属性有 课程名，学习周期，价格)
	def __init__(self, name, cycle, price):
		self.name = name
		self.cycle = cycle
		self.price = price


class Classes:  # 班级类
	def __init__(self, name):
		self.name = name
	
	# 关联课程
	def relevance_coures(self, course_obj=None):
		self.course_obj = course_obj
	
	# 关联学生
	def relevance_student(self, student_obj=None):
		self.student_obj = student_obj
	
	# 关联讲师
	def relevance_teacher(self, teacher_obj=None):
		self.teacher_obj = teacher_obj


class Person:
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender


class Admin(Person):
	# 创建讲师， 创建班级，创建课程
	def creat_teacher(self):
		if self.verify():
			print('创建讲师')
	
	def creat_classes(self):
		if self.verify():
			print('创建班级')
	
	def creat_course(self):
		if self.verify():
			print('创建课程')
			
	def verify(self):
		if self.name in School.admin_lis:
			return True
		else:
			print('没有学校授权，没有权限...')
			return False


class Teacher(Person):
	# 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
	
	def select_classes(self):
		pass
	
	def dir_student_list(self):
		pass
	
	def change_score(self):
		pass


class Student(Person):
	# 可以注册， 交学费， 选择班级
	def register(self):
		print('学生注册')
	
	def pay_the_fees(self):
		print('学生缴费')
	
	def select_classes(self):
		print('学生选择班级')





# 创建学校
school_1 = School('老男孩学校', '北京')
school_2 = School('老男孩学校', '上海')


# 创建管理员
admin1 = Admin('zzq', 28, 'male')
admin2 = Admin('xcc', 27, 'female')
School.mandate(admin1)
# print(admin1.verify())
# print(admin2.verify())
# admin2.creat_teacher()

#创建课程
ret = school_1.create_course('python', 6, 10000)


