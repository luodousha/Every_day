# 1普通进度条
# import sys
# import time
# def func():
# 	for i in range(1,101):
# 		print('\r', end='')
# 		print('Download progress:{}%'.format(i), '>'*(i//2),end='')
# 		sys.stdout.flush()
# 		time.sleep(0.3)
# # func()
#
# # 带时间的进度条
# # time
# scale = 50
# print('执行开始，祈祷不报错'.center(scale//2,'-'))
# start = time.perf_counter()
# for i in range(scale+1):
# 	a = "*" * i
# 	b = "." * (scale - i )
# 	c = (i/scale) * 100
# 	dur = time.perf_counter() -start
# 	print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end='')
# 	time.sleep(0.1)
#
# print('\n'+'执行结果，万幸'.center(scale//2,'-'))

from time import sleep
from tqdm import tqdm

for i in tqdm(range(1,500)):
	sleep(0.01)
sleep(0.5)
