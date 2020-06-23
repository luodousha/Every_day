dic = {'name': '赵志强'}
dic.setdefault('hobbie', 'basketabll')
print(dic)
dic.setdefault('name', '徐聪聪')
print(dic)
L1 = ['赵志强', '徐聪聪', '李湾']
L2 = ['zzq', 'xcc', 'lw']

dic = {x: y for x, y in zip(L1, L2)}
print(dic)
# 输出结果 {'赵志强': 'zzq', '徐聪聪': 'xcc', '李湾': 'lw'}
# dic.pop('赵志强')
# print(dic)
#
# del dic['赵志强']
# del dic
# print(dic)
#
# dic.clear()
# print(dic)


t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 1, 3, 4, 5, 6)
print(1 in t )
# 输出结果 True