# _*_ coding:utf-8 _*_
import os

colume_lis = ['id', 'name', 'age', 'phone', 'dept', 'enroll_data']  # 字段列表


def check_user_in():
	'''
	检查用户输入合理性
	:return:
	'''
	select_order = ('find', 'add', 'del', 'update') # 用户输入首单词必须由此元组元素构成
	while True:
		user_in = input('请输入命令>>>>>（按q退出程序）')
		user_in_str = formart_str(user_in)  # 处理用户关键字间多余的空格，并返回以一个空格为间隔的字符串
		# print(user_in_str)  #测试 user_in_str 字符串
		keywords_list = user_in_str.strip().split(' ')
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
				add_user(str_lis = keywords_list)
				
			elif user_in.startswith('del'):
				del_user(str_lis= keywords_list)
				
			elif user_in.startswith('update'):
				update_user(str_lis=keywords_list)
				
		else:
			print('关键字错误，请重试....')
	
		
def add_user(*args,**kwargs):
	'''
	添加用户信息
	:return:
	'''
	dic_info = read_user_data()
	# print('添加用户')
	dic_value=kwargs['str_lis'][2]
	dic_value_lis = dic_value.split(',')
	if len(dic_value_lis) == 5:
		if verify_phone(dic_value_lis):
			lis = list(dic_info.keys())  # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
			max_id = int(lis[-1])+1
			dic_value_lis.insert(0, str(max_id))
			new_dic_info = {x: y for x, y in zip(colume_lis, dic_value_lis)}
			data_str_lis = list(new_dic_info.values())
			s = ','.join(data_str_lis)+'\n'
			add_data(s)
			check_user_in()
		else:
			print('电话号码重复')
	else:
		print('缺少足够参数')
		
	
def del_user(*args,**kwargs):
	'''
	根据序号删除相应的员工的信息
	:return:
	'''
	try:
		dis_info = read_user_data()
		print(kwargs['str_lis'])
		key = kwargs['str_lis'][-1]
		dis_info.pop(key)
		del_data(key)
		check_user_in()
	except KeyError as e:
		print(e)
	
	
def update_user(*args,**kwargs):
	'''
	可以根据特殊条件修改员工信息
	:return:
	'''
	dis_info = read_user_data()
	print('修改属性')
	print(kwargs['str_lis'])
	index = kwargs['str_lis'].index('where')
	lis_ = kwargs['str_lis'][index:]
	ret = compare_str(lis_, dis_info)
	for dic in ret:
		print(dic)
	
	
def find_user_info(*args,**kwargs):
	# print(kwargs)  # 接收用户的输入字符串
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
		keys = kwargs['str_lis'][1].split(',')  # 拿到筛查的keys [name.age]
		if kwargs['str_lis'][-1] == 'staff_table':  # 不加筛查条件
			for dic in filter_key(keys, dic_info):  # 将要显示的字段筛选后输出
				display(dic)
		
		if 'where' in kwargs['str_lis']:  # 加筛查条件
			index = kwargs['str_lis'].index('where')  # 切割'where'至筛查条件
			lis_ = kwargs['str_lis'][index:]  # ['where', 'age', '>', '26']
			compare_str(lis_, dic_info, keys_lis=keys)  # 这里要写一个判断的函数将筛查条件传入
			
		
def compare_str(lis, dic_info, keys_lis=None):
	'''
	判断where 条件
	:param lis: 筛查条件列表 例如['where' , 'age' , '>' ,'26' ]
	:param dic_info: 所有数据字典格式
	:param keys_lis: 筛查所需字段的列表
	:return:
	'''
	value_lis = []
	if keys_lis == None:  # 判断有没有过滤字段
		for v in dic_info.values():
			data_value = v.get(lis[1])  # 对应的值，age--> 28 ,name --> 'alex'
			# print(data_value)
			if 'like' in lis:
				# print('模糊查询...')
				if wipe_mark(lis[3]) in data_value:
					display(v)
			elif data_value.isdigit():  # 数据类型是数字字符串的时候
				if lis[2] == '>':
					if int(data_value)-int(lis[3]) > 0:  # 满足筛查条件
						display(v)
				elif lis[2] == '<':
					if int(data_value) - int(lis[3]) < 0:
						display(v)

				elif lis[2] == '>=':
					if int(data_value)-int(lis[3]) >= 0:  # 满足筛查条件
						display(v)
				elif lis[2] == '<=':
					if int(data_value) - int(lis[3]) <= 0:
						display(v)
			elif lis[1].isalpha():  # 判断字符串是否是一至的情况
				if lis[2] == '=':
					str = wipe_mark(lis[3])  # 将双引号，或是单引号去掉
					if data_value == str:
						display(v)
						value_lis.append(v)
	return value_lis
	if keys_lis:  # 判断有没有关键字列表,有就筛选显示字段
		for v in dic_info.values():
			data_value = v.get(lis[1])
			if 'like' in lis:
				if wipe_mark(lis[3]) in data_value:
					display(dic_info, keys_lis=keys_lis, value=v)
			elif data_value.isdigit():  # 数据类型是数字字符串的时候
				if lis[2] == '>':
					if int(data_value)-int(lis[3]) > 0:  # 满足筛查条件
						display(dic_info, keys_lis=keys_lis, value=v)
				elif lis[2] == '<':
					if int(data_value) - int(lis[3]) < 0:
						display(dic_info, keys_lis=keys_lis, value=v)
				# 待开发
				elif lis[2] == '>=':
					if int(data_value)-int(lis[3]) >= 0:  # 满足筛查条件
						display(dic_info, keys_lis=keys_lis, value=v)
				elif lis[2] == '<=':
					if int(data_value) - int(lis[3]) <= 0:
						display(dic_info, keys_lis=keys_lis, value=v)
			elif lis[1].isalpha():  # 判断字符串是否是一至的情况
				if lis[2] == '=':
					str = wipe_mark(lis[3])  # 将双引号，或是单引号去掉
					if data_value == str:
						display(dic_info, keys_lis=keys_lis, value=v)
				

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
	str_lis2 = str_lis[:] # 遍历原列表删除新列表
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
	# colume_lis = ['id', 'name', 'age', 'phone', 'enroll_dept', 'date']  # 字段列表
	with open('staff_table','r',encoding='utf-8') as f:
		line = f.readlines()
		for i in line:
			value = i.strip().split(',')
			dic_info[value[0]] = {x : y for x, y in zip(colume_lis, value)}
		# print(dic_info)
	return dic_info


def add_data(str):
	'''
	新增数据
	:return:
	'''
	with open('staff_table', 'a', encoding='utf-8') as f:
		f.write(str)
		f.flush()

	
def del_data(key):
	with open('staff_table', 'r', encoding='utf-8') as f:
		with open('staff_table_new','w',encoding='utf-8')as f2:
			for line in f:
				lis = line.split(',')
				if lis[0] == key:
					pass
				else:
					f2.write(line)
		f2.close()
	f.close()
	os.replace('staff_table_new','staff_table')


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


def display(dic_info,keys_lis=None,value=None):
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
	

def run():
	'''
	主函数
	:return:
	'''
	check_user_in()


run()

