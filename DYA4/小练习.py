# 创建
# 创建方式①
dic = {'name': '赵志强', 'age': 27}
print(dic)
# 创建方式②

dic2 = dict(name = '徐聪聪', age = 27)
print(dic2)

#创建方式③
dic3 = {}.fromkeys([x for x in range( 10 )],100)
print(dic3)

# 创建方式④
# 字典推导式
l1 = ['a', 'b']
l2 = ['A', 'B']
dic4 = { x : y for x , y in  zip(l1,l2)}
print(dic4)
import  random
dic5 = { i : random.randint(0,10) for i in range(10)}
print(dic5)

# 增
# 先是查找字典字典里有没有key ,有就会返回原value ,不会创建新key ,没有就会创建新key
dic.setdefault('love','嘿嘿嘿')
print(dic)
x=dic.setdefault('name','惺惺惜惺惺')
print(x)
print(dic)

# 直接新增，假如有原key 就会修改为新值
dic['new_key'] = 'new_value'
print(dic)
dic['new_key'] = '传统手艺不能丢'
print(dic)

# 删
# 方法一 pop('key')
# 删除给定key，
dic.pop('new_key')

# 方法二 del
# del 是一种全局通用的删除，什么都能删
# 删出给定的 key
del dic['age']

# 删除字典
del dic5
# print(dic5) # 由于del 删掉了就会 报错

# 方法三 clear（）
# 清空
dic4.clear()
print(dic4) # 删掉了就剩空字典

# 方法四 popitem()
# 随机删除
dic = {1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100, 7: 100, 8: 100}
print(dic)
# 随机删除，并以元组的形式返回删除的键值对
print(dic.popitem()) # 这里假如字典是有点顺序的话，也不是随机删除
print(dic)


# 改
# ①给原key赋值，
print(dic)
dic[1] = 'gamw'
print(dic)


# ②更新 原字典原来有的key 会被更新新值，假如没有新的值就会保存
print(dic)
print(dic2)

dic.update(dic2)
print(dic)
print(dic3)
dic.update(dic3)

# 查
# ①查key 是否在字典里
# dic[key] # 直接查，假如没有就会报错
# print(dic2['name'])

# ② git(key)
# get 尝试获取 key ，假如存在，就返回 value ,不存在就返回默认值 None,默认值可以修改

print(dic.get('namew'))
print(dic)

# 查找字典的所有 key 值
print(dic.keys())

#  查找字典所有的 values 值
print(dic.values())

# 查找字典所有的键值对 (key,value)
print(dic.items())

# 查看key 是否在 字典中
print('name' in dic) # 返回布尔值 判断key是否存在字典中

# 循环

# 直接取key ,value
# 官方推荐
for k in dic:
	print(k,dic[k])

#循环取 key,得到value
for k in dic.keys():
	print(k,dic[k])
	
# 循环取value
for v in dic.values():
	print(v)

# 循环取键值对
for k , v in dic.items():
	print(k,v)


# 练习 1
# 用你能想到的最少的代码生成一个包含100个key的字典，每个value的值不能一样
import random
# 这个方法不行，这个方法的值是一样的
dic = {}.fromkeys([x for x in range (100) ],random.randint(1,100))
print(dic)
# 列表推导式：
dic = {x:y for x , y in zip([x for x in range(0,100)],[y for y in range(100,200)])}
print(dic)
print(len(dic.values()))

# 练习2
'''
{‘k0’: 0, ‘k1’: 1, ‘k2’: 2, ‘k3’: 3, ‘k4’: 4, ‘k5’: 5, ‘k6’: 6, ‘k7’: 7, ‘k8’: 8, ‘k9’: 9}
请把这个dict中key大于5的值value打印出来。
'''
dic = {'k0': 0, 'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5, 'k6': 6, 'k7': 7, 'k8': 8, 'k9': 9}
for k in dic:
	if dic[k] > 5:
		print(dic[k])
		
# 练习3
'''
把题2中value是偶数的统一改成-1
'''
for k in dic:
	if dic[k] % 2 == 0 :
		dic[k] = -1
print(dic)

# 题四
'''
请设计一个dict, 存储你们公司每个人的信息，
信息包含至少姓名、年龄、电话、职位、工资，
并提供一个简单的查找接口，用户按你的要求
输入要查找的人，你的程序把查到的信息打印
出来
'''
# dic = {user_name:[username,age,phone,position ,salary]}
dic = {}
while True:
	# print(dic)
	print('欢迎进入员工查询系统'.center(50,'-'))
	msg = '''
	功能详情：
			1：查询所有员工信息
			2：添加新员工信息
			3：查询某员工信息
			4：退出
	'''
	print(msg,end='\t')
	user = input('请选择功能：')
	if user.isdigit():
		user = int(user)
		if user is 1:
			for k in dic:
				print(k,dic[k])
		elif user is 2:
			user_name = input('请输入新增员工')
			age = int(input('请输出员工年纪'))
			user_phone = input('请输入电话号码')
			user_position = input('请输入员工职位')
			user_salary = int(input('请输入薪资'))
			# dic = {}
			dic.setdefault(user_name, [user_name, age, user_phone, user_position, user_salary])
			dic.update(dic)
		elif user is 3:
			user_name = input('请输入员工姓名：')
			value = dic.get(user_name)
			if not value:
				print('不存在该员工！')
			else:
				print(value)
		elif user is 4:
			exit()
		else:
			print('待开发，请重现选择功能！')
	else:
		print('不存在此功能')
		
		