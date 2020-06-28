# 变量
count = 0 # 统计查询的计数
dic = {}
with open('stock_data.txt','r',encoding='utf-8') as f:
	column =  f.readline().strip().split(',') # 获取数据key
	for line in f:
		line = line.strip().split(',')
		dic[line[2]] = line
while True:
	print('股票查询系统'.center(66, '-'))
	print('【程序功能】 【1模糊查询】【2筛查最新价、涨跌幅、换手率】【3按q退出程序】')
	user_in = input('程序查寻接口>:')
	if not user_in.strip():
		print('输入错误，不允许输入空值')
		continue
	elif user_in.upper() == 'Q':
		print('Bay! 欢迎再次使用查询。')
		
	