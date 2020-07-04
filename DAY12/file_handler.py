colume_lis = ['id', 'name', 'age', 'phone', 'dept', 'date']  # 字段列表
def check_user_in():
	'''
	查找用户的信息
	:return:
	'''
	select_order = ('find', 'add', 'del', 'update')
	while True:
		user_in = input('*-关键字至少需要一个空白间隔-* >> ')
		user_in_str = formart_str(user_in)  # 处理多余的空格，并返回一个一个空格
		print(user_in_str)
		keywords_list = user_in_str.strip().split(' ')
		# print(keywords_list)  # test
		if not user_in:
			print('不允许输入空值')
			continue
		elif user_in.upper() == 'Q':
			print('欢迎再次使用本程序...')
			exit()
		if user_in.startswith(select_order):  # 命名开头必须是select_order中的元素
			if user_in.startswith('find'):
				find_user_info(str_lis=keywords_list)  # 将输入的类表传入查找函数
			elif user_in.startswith('add'):
				add_user()
			elif user_in.startswith('del'):
				del_user()
			elif user_in.startswith('update'):
				update_user()
		else:
			print('Type Error ,place try again.')
		
def add_user(*args,**kwargs):
	'''
	添加用户信息
	:return:
	'''
	print('添加用户')


def del_user(*args,**kwargs):
	'''
	删除用户信息
	:return:
	'''
	print('删除用户')
	

def update_user(*args,**kwargs):
	'''
	修改用户信息
	:return:
	'''
	print('更新用户')
	
def display(*args,**kwargs):
	'''
	答应输出，查询结果
	:return:
	'''
	print('显示模块')
	dic = read_user_data()

def find_user_info(*args,**kwargs):
	print(kwargs)  # 接收用户的输入字符串
	dic_info = read_user_data()
	if kwargs['str_lis'][1] == '*':  # 拿所有数据匹配
		if kwargs['str_lis'][-1] == 'staff_table':  # 没有筛查条件的情况
			for v in dic_info.values():
				lis = list(v.values())
				print(' '.join(lis))  # 输出打印所有数据的情况
			
		if 'where' in kwargs['str_lis']:
			index = kwargs['str_lis'].index('where')
			lis_ = kwargs['str_lis'][index:]
			print(lis_)
			for v in dic_info.values():
				# print(v[lis_[1]],type(v[lis_[1]]))
				if v[lis_[1]].isdigit():
					# v  = int(v[lis_[1]])
					s = v[lis_[1]] + lis_[2] + lis_[3]
					if eval(s):
						display(v)
				else:
					pass
					
	else:  # 筛查列表是其他参数,不是 * 的情况
		keys = kwargs['str_lis'][1].split(',') # 拿到筛查的key
		print(keys)
		if kwargs['str_lis'][-1] == 'staff_table':  # 不加筛查条件
			pass
		if 'where' in kwargs['str_lis']:  # 加筛查条件
			pass
		
def formart_str(str):
	'''
	格式化用户输入，允许用户多空格输入，但必须有一个空格
	:param str:原str可能保留很多无效空格
	:return: 返回一个只有一个空格隔开的str
	'''
	str_lis = str.split(' ')
	str_lis2 = str_lis[:] # 遍历原列表删除新列表
	for i in str_lis:
		if i == '':
			str_lis2.remove(i)
	str = ' '.join(str_lis2)
	return str

def read_user_data():
	'''
	将文件数据装换为dict
	:return: dic
	'''
	dic_info = {}  # 以字典的形式保存用户信息
	# colume_lis = ['id', 'name', 'age', 'phone', 'enroll_dept', 'date']  # 字段列表
	with open('staff_table','r',encoding='utf-8') as f:
		line = f.readlines()
		for i in line:
			value = i.strip().split(',')
			dic_info[value[0]] = {x : y for x, y in zip(colume_lis, value)}
		# print(dic_info)
	return dic_info

def display(dis):
	'''
	显示数据
	:param dis:
	:return:
	'''
	lis = list(dis.values())
	print(' '.join(lis))

def run():
	'''
	主函数
	:return:
	'''
	pass

if __name__ == '__main__':
	check_user_in()
	