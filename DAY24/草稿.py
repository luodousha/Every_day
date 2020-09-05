import pickle
import sys

class Admin:
	def __init__(self,name):
		self.name = name
		
	def create_courses(self):
		print('创建课程')

	def create_students(self):
		print('创建学生')
		
	def create_teachers(self):
		print('创建讲师')
		
	def create_chasses(self):
		print('创建班级')
		
	def create_school(self):
		print('创建学校')
		
	def exit(self):
		exit()
		
		
class Student:
	def __init__(self,name):
		self.name = name
		
	def register(self):
		print('注册')
		
	def select_course(self):
		print('选择课程')
	
	def check_course(self):
		print('查看课程')
		
	def select_classes(self):
		print('选择班级')
		
	def pay_money(self):
		print('缴费')
	
	
	def exit(self):
		exit()
	

def login():
	user_name = input('username:')
	user_pwd = input('passwword:')
	with open('user_info', 'r', encoding='UTF-8') as f:
		for line in f:
			line = line.strip().split(',')
			name, pwd, identify = line  # identify身份识别
			if user_name == name and user_pwd == pwd:
				print('登录成功！欢迎%s'% name)
				obj = Admin(name)
				obj.identify = identify
				return {'name': obj.name, 'identify': obj.identify,'result':True,'obj':obj}
			# if user_name != name or user_pwd != pwd:
				# print('用户名或密码错误....')
				# return {'name':user_name,'result':False}
	
	
def func(cls):
	lis = []
	for k in cls.__dict__:
		if '__' not in k:
			lis.append(k)
	lis=list(enumerate(lis,1))
	for i in lis:
		print(f'{i[0]}:{i[1]}')
	return lis

ret = login()
if ret['result']:
	s = ret['identify']
	if hasattr(sys.modules[__name__],s.capitalize()):
		cls = getattr(sys.modules[__name__],s.capitalize())
		func(cls)
		user_in = input('请选择序号：')
		if isinstance(user_in, int):
			user_in = user_in - 1
			str = func(cls)[user_in][1]
		# print(f)
		# if hasattr(func(cls)[user_in][1]):
			getattr(cls, str)(ret['obj'])
		else:
			print('序号只能为数字整型...')





















# s = '我是黑人之神'
# g=s.encode() # str ---- > 转换为bytes模式 编码
# print(g,type(g))
# print(g.decode()) # bytes----> 装换为str模式 解码

# dic = {'Name':'zzq'}
# s = '我是大笨猪'
# str_dic = pickle.dumps(dic)
# print(str_dic,type(str_dic))
# kk = pickle.loads(str_dic)
# print(kk,type(kk))

# s_b = pickle.dumps(s)
# print(s_b,type(s_b))
# print(s_b.decode('utf-8'))
# ss=json.dumps(dic)
# print(ss,type(ss))
# print(json.loads(ss))

# s = Student('赵志强')
# print(s.name)
# s = {'name': 'zzq', 'identify': 'student', 'pwd': '123'}
# s_b = pickle.dumps(s)
# print(s_b,type(s_b))
# with open(file='test', mode='wb') as f:
# 	f.write(s_b)
#
# with open('test',mode='rb')as f2 :
# 	for line in f2:
# 		line = line.strip()
# 		dic = pickle.loads(line)
# 	print(dic)