# _*_ coding:utf-8 _*_
import os

colume_lis = ['id', 'name', 'age', 'phone', 'dept', 'enroll_data']  # 字段列表


def check_user_in():
	'''
	检查用户输入合理性
	:return:
	'''
	select_order = ('find', 'add', 'del', 'update')  # 用户输入首单词必须由此元组元素构成
	while True:
		user_in = input(r'请输入命令>>>>>（按q退出程序）')
		user_in_str = formart_str(user_in)  # 处理用户关键字间多余的空格，并返回以一个空格为间隔的字符串
		# print(user_in_str)  #测试 user_in_str 字符串
		keywords_str = user_in_str.strip()
		keywords_list = deal_with_user_in(keywords_str)
		# print(keywords_list)  # test 测试 用户关键字列表
		if not user_in.strip():
			print('不允许输入空值')
			continue
		elif user_in.upper() == 'Q':  # 程序出口
			print('欢迎再次使用本程序...')
			exit()
		if user_in.startswith(select_order):  # 判断首单词是find 调用find_user_info 函数
			if user_in.startswith('find'):
				find_user_info(str_lis=keywords_list)  # 将用户查询语句传入
			
			elif user_in.startswith('add'):
				add_user(str_lis=keywords_list)
			
			elif user_in.startswith('del'):
				del_user(str_lis=keywords_list)
			
			elif user_in.startswith('update'):
				update_user(str_lis=keywords_list)
		
		else:
			print('关键字错误，请重试....')


def add_user(*args, **kwargs):
	'''
	添加用户信息
	:return:
	'''
	dic_info = read_user_data()
	# print('添加用户')
	dic_value = kwargs['str_lis'][2]
	dic_value_lis = dic_value.split(',')
	if len(dic_value_lis) == 5:
		if verify_phone(dic_value_lis):
			lis = list(dic_info.keys())  # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
			max_id = int(lis[-1]) + 1
			dic_value_lis.insert(0, str(max_id))
			new_dic_info = {x: y for x, y in zip(colume_lis, dic_value_lis)}
			data_str_lis = list(new_dic_info.values())
			s = ','.join(data_str_lis) + '\n'
			add_data(s)
			check_user_in()
		else:
			print('电话号码重复')
	else:
		print('缺少足够参数')


def del_user(*args, **kwargs):
	'''
	根据序号删除相应的员工的信息
	:return:
	'''
	try:
		dis_info = read_user_data()
		# print(kwargs['str_lis'])
		key = kwargs['str_lis'][-1]
		dis_info.pop(key)
		del_data(key)
		check_user_in()
	except KeyError:
		print('不存在数据...')
	finally:
		run()


def update_user(*args, **kwargs):
	'''
	可以根据特殊条件修改，替换员工信息
	:return:
	'''
	dis_info = read_user_data()
	# print('修改属性')
	index_where = kwargs['str_lis'].index('where')
	index_set = kwargs['str_lis'].index('set')
	alter_lis = kwargs['str_lis'][index_set + 1].split('=')  # 获取修改参数的下标
	new_str = wipe_mark(alter_lis[1])  # 修改后的数据
	alter = wipe_mark(alter_lis[0])  # 需要修改的字段
	lis_ = kwargs['str_lis'][index_where:]
	ret = compare_str(lis_, dis_info)
	for v in ret:
		old_str = v.get(alter)
		# print(old_str)
		replace_str(old_str, new_str)
	os.replace('staff_table_new', 'staff_table')
	
	
def replace_str(old_str,new_str):
	'''
	替换字符串
	:param old_str: str 被替换的字符串
	:param new_str:str  替换的字符串
	:return:
	'''
	f  = open_file('r')
	f2 = open_file('w')
	for line in f:
		# print(line)
		if old_str in line.split(','): # 这里分割避免字符串包含替换内容的情况
			line=line.replace(old_str,new_str)
		f2.write(line)
	f2.close()
	f.close()

	
def find_user_info(*args, **kwargs):
	'''
	查询用户输入
	:param args:
	:param kwargs:切割处理后的用户关键字输入列表
	:return:
	'''
	# print(kwargs)  # test接收用户的输入
	dic_info = read_user_data()
	if kwargs['str_lis'][1] == '*':  # 拿所有数据匹配
		if kwargs['str_lis'][-1] == 'staff_table':  # 没有筛查条件的情况
			for v in dic_info.values():
				display(v)
		if 'where' in kwargs['str_lis']:
			index = kwargs['str_lis'].index('where')  # 切割'where'至筛查条件
			lis_ = kwargs['str_lis'][index:]  # ['where', 'age', '>', '26']
			compare_str(lis_, dic_info)  # 这里要写一个判断的函数将筛查条件传入
	
	else:  # 筛查列表是其他参数,不是 * 的情况
		if len(kwargs['str_lis'][1]) > 1:
			keys = kwargs['str_lis'][1].split(',')  # 拿到筛查的keys [name,age]
		else:
			keys = kwargs['str_lis'][1]
		if kwargs['str_lis'][-1] == 'staff_table':  # 不加筛查条件
			for dic in filter_key(keys, dic_info):  # 将要显示的字段筛选后输出
				display(dic)
		
		elif 'where' in kwargs['str_lis']:  # 有参数列表有筛查条件
			index = kwargs['str_lis'].index('where')  # 切割'where'至筛查条件
			lis_ = kwargs['str_lis'][index:]  # ['where', 'age', '>', '26']
			compare_str(lis_, dic_info, keys_lis=keys)  # 这里要写一个判断的函数将筛查条件传入
	

def compare_str(lis, dic_info, keys_lis=None):
	'''
	判断where 条件
	:param lis: 筛查条件列表 例如['where' , 'age' , '>' ,'26' ]
	:param dic_info: 所有数据的字典类型
	:param keys_lis: 筛查需要显示字段的列表
	:return: 返回满足筛查条件的字典元素列表
	'''
	value_lis = [] # 用来储存满足条件的字典对象
	if keys_lis == None:  # 没有过滤字段的情况
		for v in dic_info.values():
			data_value = v.get(lis[1])  # 获取筛选关键字
			# print(data_value)
			if 'like' in lis:  # 判断是否是有关键字'like'
				if wipe_mark(lis[3]) in data_value:  # 将双引号，单引号去除
					display(v)
			elif data_value.isdigit():  # 字段的数据类型是数字字符串的时候 例如age.id
				if lis[2] == '>':
					if int(data_value) - int(lis[3]) > 0:  # 满足筛查条件
						display(v)
				
				elif lis[2] == '<':
					if int(data_value) - int(lis[3]) < 0:
						display(v)
				
				elif lis[2] == '>=':
					if int(data_value) - int(lis[3]) >= 0:
						display(v)
				
				elif lis[2] == '<=':
					if int(data_value) - int(lis[3]) <= 0:
						display(v)
			
			elif lis[1].isalpha():  # 判断字符串是否是一至的情况
				if lis[2] == '=':
					str = wipe_mark(lis[3])  # 将双引号，或是单引号去掉
					# str = wipe_mark(str)
					if data_value == str:
						display(v)
						value_lis.append(v)  # 将符合条件的数据添加到列表中
		return value_lis  # 返回字符串一至的所有数据 比如返回 部门都是'IT'
	
	if keys_lis:   # 有关键字列表,只显示关键字字段 如只显示 name,age 字段内容
		for v in dic_info.values():
			data_value = v.get(lis[1])
			if 'like' in lis:
				if wipe_mark(lis[3]) in data_value:
					display(dic_info, keys_lis=keys_lis, value=v)
			elif data_value.isdigit():  # 字段数据类型是数字字符串的时候
				if lis[2] == '>':
					if int(data_value) - int(lis[3]) > 0:  # 满足筛查条件
						display(dic_info, keys_lis=keys_lis, value=v)
				elif lis[2] == '<':
					if int(data_value) - int(lis[3]) < 0:
						display(dic_info, keys_lis=keys_lis, value=v)
				elif lis[2] == '>=':
					if int(data_value) - int(lis[3]) >= 0:  # 满足筛查条件
						display(dic_info, keys_lis=keys_lis, value=v)
				elif lis[2] == '<=':
					if int(data_value) - int(lis[3]) <= 0:
						display(dic_info, keys_lis=keys_lis, value=v)
			elif lis[1].isalpha():  # 判断字符串是否是一至的情况
				if lis[2] == '=':
					str = wipe_mark(lis[3])  # 将双引号，或是单引号去掉
					if data_value == str:
						display(dic_info, keys_lis=keys_lis, value=v)
						value_lis.append(v)
		return value_lis


def wipe_mark(str):
	"""
	将字符串的双引号，或单引号去除
	:param str:
	:return:
	"""
	if str.startswith('\'') or str.startswith('"') and str.endswith('\'') or str.endswith('"'):
		str = str[1:-1]
	else:
		return str
	return str


def formart_str(str):
	'''
	格式化用户输入，允许用户多空格输入，但必须有一个空格
	:param str:原str可能保留很多无效空格
	:return: 返回一个只有一个空格隔开的str
	'''
	str_lis = str.split(' ')
	# print(str_lis)
	str_lis2 = str_lis[:]  # 遍历原列表删除新列表
	for i in str_lis:
		if i == '':
			str_lis2.remove(i)
	str = ' '.join(str_lis2)
	return str


def read_user_data():
	'''
	将文件数据装换为dict类型
	:return: dic_info
	'''
	dic_info = {}  # 以字典的形式保存用户信息
	# with open('staff_table', 'r', encoding='utf-8') as f:
	f = open_file('r')
	line = f.readlines()
	for i in line:
		value = i.strip().split(',')
		dic_info[value[0]] = {x: y for x, y in zip(colume_lis, value)}
	return dic_info


def add_data(str):
	'''
	新增数据
	:return:
	'''
	# with open('staff_table', 'a', encoding='utf-8') as f:
	f = open_file('a')
	f.write(str)
	f.flush()
	f.close()


def del_data(key):
	f = open_file('r')
	f2 = open_file('w')
	for line in f:
		lis = line.split(',')
		if lis[0] == key:
			pass
		else:
			f2.write(line)
	f2.close()
	f.close()
	os.replace('staff_table_new', 'staff_table')


def filter_key(keys, dic_info):
	'''
	筛选要输出的字段
	:param keys: 需要输出的字段
	:param dic: 全部数据
	:return: 返回list类型 包含输出字段的信息
	'''
	lis = []
	for v in dic_info.values():
		def inter(v):
			dic = {}
			for i in keys:
				dic[i] = v[i]
			return dic
		
		ret = inter(v)
		lis.append(ret)
	return lis  # 返回筛选字段组成的字典的列表类型


def deal_with_user_in(user_in_str):
	'''
	处理输入字符串最后的元素包含空格符情况
	:param user_in_str: 用户输入字符串
	:return: list tpye 保留最后一个空格的的列表或者用户输入命令切割列表
	'''
	# print(user_in_str) # test
	user_in_str = user_in_str.strip()  # 去除两边空白
	space_num = user_in_str.count(' ')  # 统计空格次数
	if 'where' in user_in_str:
		where_index =user_in_str.index('where')
		if 'name' in user_in_str[where_index:]:
			user_in_str_list = user_in_str.split(' ', space_num - 1)
			return user_in_str_list
		return user_in_str.split(' ')
	else:
		return user_in_str.split(' ')


def display(dic_info, keys_lis=None, value=None):
	'''
	显示字段
	:param dic_info: 所有数据的字典集合
	:param keys_lis: 需要筛选字段的列表
	:param value: 筛查字段的数据
	:return:
	'''
	if keys_lis == None:
		for k, value in dic_info.items():
			print(k, value, end=' ')  # 显示数据，每个数据间隔一个空格
		print()
	
	if keys_lis:
		for i in keys_lis:
			print(i, value[i], end=' ')
		print()
		

def verify_phone(lis):
	'''
	校验电话号码是否唯一
	:return: bool
	'''
	dic_info = read_user_data()
	for v in dic_info.values():
		value = v.get('phone')
		if value == lis[2]:
			return False
	else:
		return True


def open_file(mode):
	if mode == 'w':
		file_name = 'staff_table_new'
	else:
		file_name = 'staff_table'
	f = open(file_name, mode,encoding='utf-8')
	return f


def run():
	'''
	运行函数
	:return:
	'''
	check_user_in()


run()
