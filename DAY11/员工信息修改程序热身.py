def login(func):
	print('登录模块')
	user_name = input('请输入用户名:')
	user_password = input('请输入密码：')
	dic = func()  # 获取用户字典，判断用户名是否存在
	user_info = dic.get(user_name)  # 尝试获取用户名，判断是否有以注册用户名
	# print(dic) # test dic
	#{'alex': {'username': 'alex', 'password': 'abc123'}}
	if user_name in dic:
		if user_password == user_info['password']:
			home(dic,user_name)  # 登录成功进入修改用户信息等其他操作
		elif user_password != user_info['password']:
			print('用户名密码错误')
	elif user_info == None:
		print(f'不存在{user_name},是否需要注册？y/n')
		select = input('')
		if select.lower() == 'y':
			register()
		else:
			print('欢迎再次使用,Bay！')
			exit()
def register():
	'''
    注册
    :return:
    '''
	print('欢迎进入注册模块')
	pass
def change_personal_info():
	'''
	修改用户信息
	:return:
	'''
	print('修改信息')


def read_data():
	'''
	读取用户信息，以字典形式返回
	:return: 用户
	'''
	dic = {}
	with open('user_info', 'r', encoding='utf-8') as f:
		column = f.readline().strip().split(',')  # 得到行首
		for line in f.readlines():
			line = line.strip().split(',')
			# print(line) # test
			dic.setdefault(line[0], {x: y for x, y in zip(column, line)})
			# print(dic)
	return dic


def home(dic,name):
	'''
	登录成功后进行的其他操作
	:param dic: 用户字典
	:param name: 用户名
	:return:
	'''
	print(f'欢迎{name}')
	print('功能1')
	print('功能2')


def run():
	print('欢迎使用员工信息修改程序v1.0'.center(58,'-'))
	print('程序说明'.center(66,'-'))
	print('1:登录')
	print('2:注册')
	print('3:退出')
	user_in = input()
	if not user_in.strip():
		print('用户输入不能为空!')
	if not user_in.isdigit():
		print('请选择数字')
		exit()
	if int(user_in) == 1:
		login(read_data)
	elif int(user_in) == 2:
		register()
	else:
		print('选择功能错误请重试!')

if __name__ == '__main__':
	run()
    
    

        