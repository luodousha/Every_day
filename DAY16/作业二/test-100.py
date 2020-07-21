#  先完成作业的前100条记录
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

def read_data():
	"""
	获取符合正则的请求的列表
	:return:
	"""
	regex = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\[(.*?)\s\+.*?\/(.*?)\sHTTP.*?(M.*?Build?|M.*?\))"
	r = re.compile(regex)
	lis = []
	f = open('网站访问日志（utf-8）.txt', 'r', encoding='utf-8')
	count = 0
	for line in f:
		count += 1
		line = line.strip()
		ret = r.search(line)
		if ret:
			lis.append(ret)
	return lis # 得到一个符合要求的列表，元素为每个pv


def calculate_pv_uv():
	'''
	统计共pv,uv
	:return:
	'''
	print(''.center(50,'='))
	ret = read_data()
	lis = []  #创建列表来保存id
	for i in ret:
		lis.append(i.group(1))
	pu_num = len(ret)
	uv_num = len(set(lis))
	print(f'总pv是{pu_num},总uv是{uv_num}')
	return lis


def select_func():
	msg =\
	'''
欢迎使用日志查询系统
根据选择序号选择功能查询功能
功能（1）查询总日志文件的总pv,总uv
功能（2）列出全天每小时的pv、uv数
功能（3）列出top 10 uv的IP地址，以及每个ip的pv点击数
功能（4）列出top 10 访问量最多的页面及每个页面的访问量
功能（5）列出访问来源的设备列表及每个设备的访问量
	'''
	print(msg.strip())
	print(''.center(50,'-'))
	user_in = input('请选择功能序号，按q/Q退出')
	if not user_in.strip():
		print('不允许输入空')
	if user_in.upper() == 'Q':
		print('欢迎下次继续使用')
		exit()
	if not user_in.isdigit():
		print('请输入功能序号')
		run()
	elif user_in.strip() == '1':
		calculate_pv_uv()
	elif user_in.strip() == '2':
		pass
	elif user_in.strip() == '3':
		pass
	elif user_in.strip() == '4':
		pass
	elif user_in.strip() == '5':
		pass
	else:
		print('输入错误，请重试...')


def every_hour_pv_uv():
	pass


def change_mouth():
	month_dic = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sept': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
	ret = read_data()
	dic = dict.fromkeys((x for x in range(24)), [])
	lis = []
	for i in ret:
		old_mouth_str = re.findall(r'[A-Za-z]{3,}', i.group(2))[0]
		mouth_str =  month_dic.get(old_mouth_str)
		new_mouth_str = i.group(2).replace(old_mouth_str, mouth_str)
		t = time.strptime(new_mouth_str, '%d/%m/%Y:%H:%M:%S')
		for k in dic.keys():
			if int(t.tm_hour) == k:
				lis.append(i)
				dic[k] = lis
	return dic

	
def create_hour_lis():
	pass


def run():
	"""
	主运行函数
	:return:
	"""
	select_func()
	
if __name__ == '__main__':
	# run()
	every_hour_pv_uv()
	a=change_mouth()
	# print(len(a[1]))