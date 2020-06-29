# 变量
dic = {}
lis = ['>', '<', '>=', '<=', '=']

with open('stock_data.txt','r',encoding='utf-8') as f:
	column = f.readline().strip().split(',') # 获取数据key
	for line in f:
		line = line.strip().split(',')
		dic[line[2]] = line
		# print(dic)
while True:
	count = 0
	print('股票查询系统'.center(66, '-'))
	print('【程序功能】 【1模糊查询】【2筛查最新价、涨跌幅、换手率】【3按q退出程序】')
	user_in = input('程序查寻接口>:')
	if not user_in.strip():
		print('输入错误，不允许输入空值')
		continue
	elif user_in.upper() == 'Q':
		print('Bay! 欢迎再次使用查询。')
	else:
		for k in dic:
			if user_in in k:
				print(dic[k])
				count += 1
		for k in dic:
			for i in lis:
				if i in user_in:
					new_dic_key = user_in.split(i)[0]
					user_in_value = user_in.split(i)[1]
					if new_dic_key in ['换手率', '涨跌幅', '振幅', '成交量(手)', '成交额']:
						value = dic[k][column.index(new_dic_key)][:-1]
					else:
						value = dic[k][column.index(new_dic_key)]
					s = value + i + user_in_value
					if eval(s):
						print(dic[k])
						count += 1
		
		print(f'已找到数据{count}条')
				
			
	
		