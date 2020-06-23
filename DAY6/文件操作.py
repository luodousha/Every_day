# _*_ coding:utf-8 _*_

# 文件操作读取

# f = open('filename', 'w', encoding='UTF-8')
# f.write('黑鬼是xxx'+'\n')
# f.close()

# f = open ('兼职白领学生空姐模特护士联系方式.txt','r',encoding='utf-8')
# print(f.read())
# print('分割符'.center(50,'-'))
#
# print(f.tell())# 打印光标的位置
# f.seek(0)#设定光标的位置
# print(f.readline()) # 打印一行
# f.close()

# f = open ('兼职白领学生空姐模特护士联系方式.txt','a',encoding='utf-8')
# f.write('黑呵呵黑泥\n')
# print(f.tell())
# f.seek(0)
# f.close()
import os

file_old = '兼职白领学生空姐模特护士联系方式.txt'
file_new = '兼职白领学生空姐模特护士联系方式.txt.new'
f = open(file_old, 'r',encoding='utf-8')
f2 = open( file_new, 'w',encoding='utf-8')
old_str = '北京'
new_str = '温州'
count = 0
for line in f: # 遍历文件
	if old_str in line :
		line = line.replace(old_str, new_str)
		count += 1
	f2.write(line)
f.close()
f2.close()
print(count)

os.replace(file_new , file_old)