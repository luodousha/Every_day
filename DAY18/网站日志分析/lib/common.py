import re

import time

import copy

def read_data():
	"""
	获取符合正则的请求的列表
	:return:
	"""
	pv_dic = {'id': [], 'request_time': [], 'url': [], 'equipment': []}
	regex = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\[(.*?)\s\+.*?\/(.*?)\/?\sHTTP.*?(Mozilla.*?Build?|Mozilla.*?\))"
	
	r = re.compile(regex)
	f = open('网站访问日志.txt', 'r', encoding='utf-8')
	for line in f:
		line = line.strip()
		ret = r.search(line)
		if ret:
			pv_dic['id'].append(ret.group(1))
			pv_dic['request_time'].append(ret.group(2))
			pv_dic['url'].append(ret.group(3))
			pv_dic['equipment'].append(ret.group(4))
	return pv_dic  # 得到一个符合正则要求的列表，元素为每个pv


def count_hour_pv():
	'''
	以字典形式，保存每个小时的pv数
	:return:
	'''
	
	def count_hour_dic(i, dic):
		for n in dic:
			if i[1] == n:  # pv的小时与字典的key值相等就存入相应的列表
				dic[n].append(i[0])  # 将相应的pv存入对应的key为小时的列表
		return dic
	
	ret = get_pv_hour()
	lis = create_hour_lis()
	l = [x for x in range(24)]
	dic = {x: y for x, y in zip(l, lis)}
	for i in ret:
		every_hour_dic = count_hour_dic(i, dic)
	return every_hour_dic


def get_pv_hour():
	'''
	得到一个列表，以元组形式包含pv与hour
	:return:list 返回一个列表元素为pv和时间组成的元组
	'''
	lis = []
	dic = read_data()
	month_dic = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8',
	             'Sept': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
	for i in dic['request_time']:
		old_mouth_str = re.search(r'[A-Za-z]{3,}', i).group()
		mouth_str = month_dic.get(old_mouth_str)
		new_mouth_str = i.replace(old_mouth_str, mouth_str)
		t = time.strptime(new_mouth_str, '%d/%m/%Y:%H:%M:%S')  # 将字符串转化为时间元组形式
		t_hour = t.tm_hour  # 获取每个pv的小时
		lis.append((i, t_hour))
	return lis


def create_hour_lis():
	'''
	创建一个列表，元素为空列表用来储存每个小时的pv
	:return:list
	'''
	lis = []
	l = [x for x in range(24)]
	for i in l:
		lis.append([])
	return lis


def get_top_dic(gruop_num):
	'''
	获取一个字典字段为正则组别与对应的次数
	:param gruop_num: 正则分组的组别
	:return:返回一个dict类型
	'''
	dic = {}
	dic_k = {
		1: 'id',
		2: 'request_time',
		3: 'url',
		4: 'equipment'
	}
	ret = read_data()
	k = dic_k.get(gruop_num)
	s = set(ret[k])
	for x in s:
		v = ret[k].count(x)
		dic[x] = v
	return dic


def catch_num_top(dic):
	'''
	返回一个字段的top 10 的列表
	:param num: 取值
	:param dic: {ip：pv}次数
	:return: list 类型 元素为 （ip,pv）
	'''
	count = 0  # 创建变量count用来计数
	lis = []
	while count < 10:
		dic2 = copy.deepcopy(dic)  # 深拷贝避免内存地址相同
		for k, v in dic.items():
			if v == max(dic.values()):
				max_num = dic2.pop(k)
				lis.append((k, max_num))
		dic = dic2
		count += 1
	return lis


def format_str():
	print(''.center(50, '-'))
