'''
pv:page visit , 页面访问量，一次请求就是一次pv
uv: user visit, 独立用户，一个ip就算一个独立用户
1 统计本日志文件的总pv、uv
2 列出全天每小时的pv、uv数
3 列出top 10 uv的IP地址，以及每个ip的pv点击数
4 列出top 10 访问量最多的页面及每个页面的访问量
5 列出访问来源的设备列表及每个设备的访问量
'''
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


def select_func():
	while True:
		msg = '''
欢迎使用日志查询系统
根据选择序号选择功能查询功能
功能（1）查询总日志文件的总pv,总uv
功能（2）列出全天每小时的pv、uv数
功能（3）列出top 10 uv的IP地址，以及每个ip的pv点击数
功能（4）列出top 10 访问量最多的页面及每个页面的访问量
功能（5）列出访问来源的设备列表及每个设备的访问量
			'''
		print(msg.strip())
		print(''.center(50, '-'))
		user_in = input('请选择功能序号，按q/Q退出')
		format_str()
		if not user_in.strip():
			print('不允许输入空值')
		elif user_in.upper() == 'Q':
			print('欢迎下次继续使用')
			exit()
		user_in = user_in.strip()
		if user_in == '1':
			calculate_pv_uv()
		elif user_in == '2':
			display_pv_uv()
		elif user_in == '3':
			display_top_field(1)
		elif user_in == '4':
			display_top_field(3)
		elif user_in == '5':
			show_device_list()
		else:
			print('输出错误请重新输入。。。')


def calculate_pv_uv():
	'''
	统计日志所有pv,uv
	:return:list类型每一个满足正则的id列表
	'''
	# lis = []  # 创建列表来保存id
	# ret = read_data()
	dic = read_data()
	pu_num = len(dic['id'])
	uv_num = len(set(dic['id']))
	print(f'日志文件pv总访问量是{pu_num}次,日志文件uv总访问是{uv_num}次')
	format_str()


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


def display_pv_uv():
	def calculate_every_uv(every_hour_pv):
		'''
		计算每个小时的up个数
		:param every_hour_pv:
		:return: int 每个小时的uv数
		'''
		s = set()
		for j in every_hour_pv:
			s.add(j)
		return len(s)
	
	ret = count_hour_pv()
	for i in range(24):
		uv_num = calculate_every_uv(ret.get(i))
		print(f'{i}小时至{i + 1}时的总pv访问是{len(ret[i])}次,总uv访问是{uv_num}次')
	format_str()


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


def display_top_field(group_num):
	'''根据正则组别，显示输出字段的top10'''
	
	ret = catch_num_top(get_top_dic(group_num))
	for i in range(1, len(ret) + 1):
		if group_num == 1:
			print(f'top{i}的访问id是{ret[i - 1][0]},pv点击数是{ret[i - 1][1]}')
		elif group_num == 3:
			print(f'top{i}的访问页面是{ret[i - 1][0]},点击数是{ret[i - 1][1]}')


def show_device_list():
	'''
	显示设备列表和设备的访问量
	:return:
	'''
	dic = get_top_dic(4)
	for k, v in dic.items():
		print(r'设备是:%s,访问量为:%s' % (k, v))
	format_str()


def format_str():
	print(''.center(50, '-'))


if __name__ == '__main__':
	select_func()
