# _*_ coding :utf-8 _*_
# 查一下如何，打印颜色....

"""
\033[显示方式;前景色；背景色m需要显示的文字\033[0m
1、显示方式：
0（默认）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
2、前景色：
30（黑色）、31（红色）、32（绿色）、 33（×××）、34（蓝色）、35（洋 红）、36（青色）、37（白色）
3、背景色:
40（黑色）、41（红色）、42（绿色）、 43（×××）、44（蓝色）、45（洋 红）、46（青色）、47（白色）
"""


# print('\033[1;32;32m game over \033[0m')


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
			if select_number in select_red :
				print(f'number {select_number} is already exist in red ball list')
				continue
			elif not 0 < select_number < 33: # 判断大小比遍历列表效率高
				print('only can select n  between 1-32 ')
				continue
			else:
				select_red.append(select_number)
		else:
			print('type error , try again !')
			continue
	elif count < 9:  # 取篮球
		msg = f'[{(count - 6)}]select blue boll:'
		select_number = input(f'\033[1;34;34m{msg}\033[0m')
		if select_number.isdigit():
			select_number = int(select_number)
			if select_number in select_blue:
				print(f'number {select_number} is already exist in blue ball list')
				continue
			elif not 0 < select_number < 17:
				print('only can select n  between 1-16 ')
				continue
			else:
				select_blue.append(select_number)
		else:
			print('type error , try again !')
			continue
	count += 1

# 输出结果
print(f'Red ball:{select_red}')
print(f'Blue ball:{select_blue}')
print('Good Luck ！')
