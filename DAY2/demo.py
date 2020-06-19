# 红，蓝球选池
red_boll_list = [x for x in range(0, 33)]
blue_boll_list = [x for x in range(0, 17)]

# 红篮球选出列表
select_red = []
select_blue = []

# 红篮球计数
count = 1
print('Welcome 小猿圈 lottery station')
# 选红蓝球
while count <= 8:  # 总共取8个球，6个红球，2个篮球
	if count < 7:  # 取红球
		msg = f'[{count}]select red boll:'
		select_number = input(f'\033[1;31;31m{msg}\033[0m')
		if select_number.isdigit():  # 判断用户输入是否是数字的字符串
			select_number = int(select_number)  # 将str类型转换为int类型
			if select_number in select_red:
				print(f'number {select_number} is already exist in red ball list')
				continue
			if select_number not in red_boll_list:
				print('only can select n  between 1-32 ')
				continue
			else:
				select_red.append(select_number)
		else:
			print('type error')
	
	elif count < 9:  # 取篮球
		msg = f'[{(count - 6)}]select blue boll:'
		select_number = input(f'\033[1;34;34m{msg}\033[0m')
		if select_number.isdigit():
			select_number = int(select_number)
			if select_number in select_blue:
				print(f'number {select_number} is already exist in blue ball list')
				continue
			if select_number not in blue_boll_list:
				print('only can select n  between 1-16 ')
				continue
			else:
				select_blue.append(select_number)
		else:
			print('type error')
			continue
	count += 1

# 选篮球
# 输出结果
print(f'Red ball:{select_red}')
print(f'Blue ball:{select_blue}')
print('Good Luck ！')
