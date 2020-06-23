import sys
import os
# print('先输入需要的替换文本')
# print('后输入替代后的文本')
# print('例如 北京 温州 北京就会被提换成北京')
lis = sys.argv  # 接收外部的输入变成一个列表
print(lis)
old_str = lis[1]
new_str = lis[2]
file_old = lis[3]
count = 0
file_new = '1'
f = open(file_old, 'r',encoding='utf-8')
f2 = open( file_new, 'w',encoding='utf-8')
for line in f:  # 遍历文件
	if old_str in line:
		line = line.replace(old_str, new_str)
		count += 1
	f2.write(line)
f.close()
f2.close()
print(count)
os.replace(file_new, file_old)





