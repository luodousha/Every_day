# 为什么序列化
# 将语言数据类型转换成一种特殊的格式，可以跨平台或者存储在数据库中
# 如何序列化
# python 主要序列化的两个模块
# 1 pikle python 特有的序列化模块
# 2 json 各种语言通用的序列化格式 但并不支持所有的数据类型，例如不支持python的集合
#序列化
#数据类型---->特殊的数据格式（json）---> 储存，或跨平台
#反序列化
#数据类型<---特殊的数据格式（json）<--- 储存，或跨平台


import json
# dump,load 针对文件
# dumps,loads 针对数据对象


# dumps,loads
#序列化
# lis = [1,2,3,4,True,False,'abc', '赵志强']
# ret_json = json.dumps(lis)
# print(ret_json,type(ret_json))
# with open('json_txt', 'wt') as f:
# 	f.write(ret_json)

#反序列化
# l = json.loads(ret_json)
# print(l, type(l))
# with open('json_txt', 'r')as f:
# 	ll=json.loads(f.readline())
# 	print(ll,type(ll))


# 针对文件（简易写法）
# load，dump
# 序列化
# with open('json_tx', 'w') as f:
	# json.dump(lis, f)  # 第一个参数是数据类型，第二个是文件句柄

# 反序列化
# with open('json_tx','r')as f:
# 	# for line in f:
# 	jj=json.load(f)
# 	print(jj)
	

# json 注意的地方
# json 格式是很多语言的通用格式可能与某种语言数据类型相像，但并不是一样的
# 例如 python    True False 'abe',或者"abe"
# json 对应的是 true,false "abe"

