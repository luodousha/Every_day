lis = ['>', '<', '=', '>=', '<=']  # 用来切割字符串
while True:
	with open('stock_data.txt', 'r', encoding='utf-8') as f:
		keys = f.readline().strip()  # 拿到keys
		keys = keys.split(',')  # 得到一个keys列表
		count = 0
		user_in = input('股票查询程序接口>:')
		
		for line in f.readlines():
			line = line.strip()  # 去空格
			value = line.split(',')
			dic = {x: y for x, y in zip(keys, value)}  # 得到每行的数据，然后存入新文件 作为新的数据来源
			if user_in in dic['名称']:
				print(dic)
				count += 1
		
			elif user_in.upper() == 'Q':
				print('Bay！')
				exit()  # 退出程序
			
			for j in lis:
				if j in user_in:
					lis2 = user_in.split(j)  # 运算符分割字符串
					if lis2[0] in ['换手率', '涨跌幅', '振幅', '成交量(手)', '成交额']:
						new_value = dic[lis2[0]][:-1]  # 将数字后方的% ,万，忆 除去
						s = new_value+j+lis2[1]  # 拼接字符串
					elif lis2[0] in ['市盈率', '量比']:  # 市盈率，量比 包含'-' 将其排除
						print('请更换筛查条件')
						exit()
					else:
						s = dic[lis2[0]] +j + lis2[1]
					if eval(s):  # 将字符串执行
						count += 1
						print(dic)  # 输出查询结果
		print('找到数据{0}条'.format(count))
	