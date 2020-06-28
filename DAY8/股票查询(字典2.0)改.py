lis = ['>', '<', '=', '<=', '>=']
dic = {}  # 定义数据类型格式
with open('stock_data.txt','r',encoding='utf-8') as f:
	column_str = f.readline().strip()
	column = column_str.split(',')
	for line in f:
		line_list=line.strip().split(',')
		dis_info = line_list[2]
		dic[dis_info] = {x: y for x, y in zip(column,line.strip().split(','))}
while True:
	count = 0
	print('股票查询'.center(80,'-'))
	print('【程序功能1：模糊查询】【程序功能2：筛查最新价、涨跌幅、换手率】 【程序结束：q】')
	user_in = input('程序查询接口>:')
	if not user_in.strip():
		continue
	elif user_in.upper() == 'Q':
		print('欢迎再次使用本程序....')
		exit()
	for k in dic:
		if user_in in k:
			print(dic[k])
			count += 1
	for i in lis:
		if i in user_in:
			key_title = user_in.split(i)[0] # 分割字符串
			value = user_in.split(i)[1]  # 分割获取数字整数或者浮点数
			# print(key_title,value)
			for key in dic.values():  # 获取各种条记录的字典
				if key_title in ['换手率', '涨跌幅', '振幅', '成交量(手)', '成交额']:
					key_str = key[key_title][:-1] # 将%号切除
				else:
					key_str = key[key_title]
				s = key_str + i + value  # 得到一个字符串包含运算符
				if eval(s):  # 将字符串 转换并判断布尔值
					count += 1
					print(key) # 输出符合筛查内容的数据
	else:
		print(f'已查找查询数据{count}条')