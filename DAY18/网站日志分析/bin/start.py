import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from core.src import *


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


if __name__ == '__main__':
    select_func()