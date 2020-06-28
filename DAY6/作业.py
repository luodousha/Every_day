# 题1
# 1、请用代码实现：利用下划线将列表的每一个元素拼接成字符串，
# li＝[‘alex’, ‘eric’, ‘rain’]
# li = ['alex','eric', 'rain']
# s = '_'.join(li) # 格式化+ 可迭代对象
# print(s)

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

'''
4、写代码，有如下列表，请按照功能要求实现每一个功能

li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
请根据索引输出“Kelly”

请使用索引找到’all’元素并将其修改为“ALL”，如：li[0][1][9]…
'''
# li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
# # print(li[2][1][-1])
# # li[2][2] = 'ALL'
# # print(li)
'''
5、有如下变量，请实现要求的功能

tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
讲述元组的特性
 # 元祖元素不能修改，元素有序不可变 ，假如可变类型嵌套在元祖里面，可以修改嵌套的元素
请问tu变量中的第一个元素“alex”是否可被修改？
# 不可以
请问tu变量中的”k2”对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
# 字符串类型 是 ,tu[1][2]['k3'] = 'Seven'
请问tu变量中的”k3”对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven“
元祖，不可以
'''
#
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# tu[1][2]['k3'] = 'Seven'
# print(tu)

'''
6、转换

将字符串s = “alex”转换成列表
lis = list(s)
将字符串s = “alex”转换成元祖
tu = tuple(s)
将列表li = [“alex”, “seven”]转换成元组
tu = tuple(li)
将元组tu = (‘Alex’, “seven”)转换成列表
li  = list(tu)
将列表li = [“alex”, “seven”]转换成字典且字典的key按照10开始向后递增
dic = dict(enumerate(li, 10))
'''
# lis = list(s)
# print(lis)
#
# s = 'alex'
# tu = tuple(s)
# print(tu)
#
# li = ['alex', 'seven']
# tu = tuple(li)
# print(tu)
#
# li  = list(tu)
# print(li)


#将列表li = [“alex”, “seven”]转换成字典且字典的key按照10开始向后递增
# li = ['alex', 'seven']
# dic = dict(enumerate(li, 10))
# print(dic)

'''
有如下值集合[11,22,33,44,55,66,77,88,99,90]，
将所有大于66的值保存至字典的第一个key中，
将小于66的值保存至第二个key的值中。
即：{‘k1’:大于66的所有值, ‘k2’:小于66的所有值}。（编程题）
'''
# dic = {'k1':[], 'k2':[]}
# # lis = [11,22,33,44,55,66,77,88,99,90]
# # for i in lis:
# # 	if i > 66:
# # 		dic['k1'].append(i)
# # 	else:
# # 		dic['k2'].append(i)
# # print(dic)

# 8、在不改变列表数据结构的情况下找最大值
li = [1,3,2,7,6,23,41,243,33,85,56]
# max_num = max(li)
# print(max_num)
max_num = li[0]
for i in li :
	if i>max_num:
		max_num=i
print(max_num)