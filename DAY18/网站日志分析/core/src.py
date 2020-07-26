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



