# 题1
# 1、请用代码实现：利用下划线将列表的每一个元素拼接成字符串，
# li＝[‘alex’, ‘eric’, ‘rain’]
li = ['alex','eric', 'rain']
s = '_'.join(li) # 格式化+ 可迭代对象
print(s)

'''
2、查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素。

li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
'''
# ①
# li = ["alec", " aric", "Alex", "Tony", "rain"]
# for i in li:
# 	i = i.strip() # 去除空格
# 	if i.startswith('A') or i.startswith('a') and i.endswith('c'):
# 		print(i)
#
# # ② 先将元组转化为字典
# tu = ("alec", " aric", "Alex", "Tony", "rain")
# li=list(tu)
# for i in li :
# 	i = i.strip()  # 去除空格
# 	if i.startswith('A') or i.startswith('a') and i.endswith('c'):
# 		print(i)

# ③
# dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
# for k in dic:
# 	v = dic[k].strip()
# 	if v.startswith('A') or v.startswith('a') and v.endswith('c'):
# 		print(k)


# 3、写代码，有如下列表，按照要求实现每一个功能
'''
li = ['alex', 'eric', 'rain']
#
# 计算列表长度并输出
print(len(li))
# 列表中追加元素“seven”，并输出添加后的列表
li.append('seven')
# 请在列表的第1个位置插入元素“Tony”，并输出添加后的列表
li.insert(0 ,'Tony')
# 请修改列表第2个位置的元素为“Kelly”，并输出修改后的列表
li[1] = 'Kelly'
print(li)
# 请删除列表中的元素“eric”，并输出修改后的列表
li.remove('eric')
print(li)
# 请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
k = li.pop(1)
print(k)
print(li)
# 请删除列表中的第3个元素，并输出删除元素后的列表
# del li[2]
print(li)
# 请删除列表中的第2至4个元素，并输出删除元素后的列表
# del li[1:5]
print(li)
# 请将列表所有的元素反转，并输出反转后的列表
# li = li.reverse()
# print(li)
# 请使用for、len、range输出列表的索引
# for i in range(len(li)):
# 	print(i)
# 请使用 enumrate 输出列表元素和序号（序号从100开始）
k=list(enumerate(li, start=100))
print(k,type(k[0]))
# 请使用for循环输出列表的所有元素
for i in li :
	print(i)
'''




