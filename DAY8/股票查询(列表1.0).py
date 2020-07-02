# 变量
#  数据格式为{'股票名称'：[每一行的数据]}
# 查询列表 ，先从行首column上获取索引
# dic['最新价'][column.index('最新价')]
dic = {}
lis = ['>', '<', '>=', '<=', '=']
with open('stock_data.txt','r',encoding='utf-8') as f:
	column = f.readline().strip().split(',') # 获取数据key
	for line in f:
		line = line.strip().split(',')
		dic[line[2]] = line
		# print(dic)
while True:
	count = 0  # 统计查询结果数量
	print('股票查询系统'.center(66, '-'))
	print('【程序功能】 【1模糊查询】【2筛查最新价、涨跌幅、换手率】【3按q退出程序】')
	user_in = input('程序查寻接口>:')
	if not user_in.strip():
		print('输入错误，不允许输入空值')
		continue
	elif user_in.upper() == 'Q':  # 程序出口
		print('Bay! 欢迎再次使用查询。')
	else:
		print(column)  # 输出首行
		for k in dic:  # 模糊查询
			if user_in in k:
				print(dic[k])
				count += 1
		for k in dic:  # 筛查条件
			for i in lis:
				if i in user_in: # 切割输入
					new_dic_key = user_in.split(i)[0]
					user_in_value = user_in.split(i)[1]
					if new_dic_key in ['换手率', '涨跌幅', '振幅', '成交量(手)', '成交额']:
						value = dic[k][column.index(new_dic_key)][:-1]  # 将百分号去除
					else:
						value = dic[k][column.index(new_dic_key)]
					s = value + i + user_in_value  # 转换成str格式
					if eval(s):  # 如果为真，就筛查满足的数据
						print(dic[k])
						count += 1
		print(f'已找到数据{count}条')
