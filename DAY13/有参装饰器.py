# 装饰器是对函数的一种功能扩展，
# 一 满足不修改调用方式
# 二 满足不修改原函数







# 比如一个主页函数我现在要新增验证
# def wrapper(func):
# 	user = input('请输入用户名:')
# 	pwd  = input('请输入密码:')
# 	if user == 'zzq' and pwd == '123':
# 		ret = func
# 	return ret
#
# # @wrapper # index = wrapper(index)
# def index():
# 	print('欢迎进入主页')


# 调用方式
# index()

# 修改调用方式
# kk = wrapper(index)
# kk()

# 装饰器装饰后偷梁换柱
# index()

# ------------------------------------------------
# 函数有返回值有参数

# def outer(func):
# 	def wrapper(*args,**kwargs):
# 		user = input('请输入用户名')
# 		pwd = input('请输入密码')
# 		if user == 'zzq' and pwd == '123':
# 			print('登录成功')
# 			ret = func(*args,**kwargs) # 接收原函数的返回值
# 			return ret
# 		else:
# 			print('用户名或密码错误')
# 	return wrapper
	
# 不加装饰器，就是直接打印字符串，然后返回a+b

# ret = home(3,9)
# print(ret)

# 给函数home加装饰器后会有验证功能

# home = wrapper(home)
# kk=home(1,3)
# print(kk)
# g=home(3,4)
# print(g)



def deco(db_type):
	def outer(func):
		def wrapper(*args,**kwargs):
			# 这里添加被装饰器前的函数，比如验证
			user = input('请输入用户名：')
			pwd = input('请输入密码')
			if db_type == 'file':
				print('基于文件验证')
				if user == 'zzq' and pwd == '123':
					ret = func(*args,**kwargs)
					return ret # 假如被装饰函数有返回值
				else:
					print('用户名或密码错误....')
			elif db_type == 'mysql':
				print('基于mysql验证')
				ret = func(*args, **kwargs)
				return ret  # 假如被装饰函数有返回值
			elif db_type == 'legb':
				print('基于legb验证')
				ret = func(*args, **kwargs)
				return ret  # 假如被装饰函数有返回值
			else:
				print('不支持验证类型')
		return wrapper # 返回wrapper内存地址，偷梁换柱
	return outer



@deco('file')
def index(a, b):
	print('欢迎到index页面')
	print(f'{a},{b}')
	return a+b
@deco('mysql')
def home():
	print('欢迎进入主页')
@deco('radies')
def register():
	print('欢迎进入注册页面')
	

# index(1,2)
# home()
register()

