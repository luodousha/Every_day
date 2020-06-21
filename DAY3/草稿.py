'''
小练习
'''

'''
针对列表names=[‘金角大王’, ‘黑姑娘’, ‘rain’, ‘eva’, ‘狗蛋’, ‘银角大王’, ‘eva’,’鸡头’]进入以下操作

通过names.index()的方法返回第2个eva的索引值

把以上的列表通过切片的形式实现反转

打印列表中所有下标为奇数的值

通过names.index()方法找到第2个eva值 ，并将其改成EVA
'''
names = ['金角大王', '黑姑娘', 'rain', 'eva', '狗蛋', '银角大王', '鸡头', 'eva']
# print(names.index('eva',4,len(names)))
# print(names[::-1])# 切片的形式反转
# print(names[1::2])# 打印下标为奇数的值
# names[-1]=names[names.index('eva',4,len(names))].upper()
# print(names)

# 首先三元三元有三个变量
# # 假设
# A = True
# D = None

# if A is True:
# 	D = 'GAME'
# else:
# 	D = 'OVER'
# print(D)

# 三元写法
# D = 'GAME' if A is True else 'OVER'
# print(D)
#
# print(names)
# names.append('赵志强')
# print(names)

# 例 在黑姑娘后面插入一个赵志强
# names = ['金角大王', '黑姑娘', 'rain', 'eva', '狗蛋', '银角大王', '鸡头', 'eva', '赵志强', '徐聪聪']
#
# del names[0]
# print(names)  # 删除了元素name[0]
# del names[0:3]  # 删除了names 中的 names[0:3] 所有元素
# print(names)
# del names # 删除了names列表
# # print(names)
# names = ['金角大王','黑姑娘','rain','eva','狗蛋','银角大王','鸡头']
# names.pop()  # 删掉最后一个元素'鸡头'
# print(names)
# names.pop(1)  # 删掉索引为1的元素 '黑姑娘'
# print(names)
# # 输出结果 ['金角大王', 'rain', 'eva', '狗蛋', '银角大王']

# names = ['金角大王','黑姑娘','rain','eva','狗蛋','银角大王','鸡头']
# names.clear()
# print(names)
# # 输出结果 []

# names = ['金角大王','黑姑娘','eva','rain','eva','狗蛋','银角大王','鸡头']
# names.remove('eva')
# print(names)

# names = ['金角大王','黑姑娘','eva','rain','eva','狗蛋','银角大王','鸡头']
# print(names.index('eva'))
# # 输出结果 2 # 说明在列表names 中有'eva'元素并且索引为2
# print(names.index('eva',3,len(names)))
# 输出结果是 4  #说明在列表name[3,7]区间中还有元素 'eva' 并输出索引下标为names中的第二个元素'eva'索引4

# names = ['金角大王','黑姑娘','eva','rain','eva','狗蛋','银角大王','鸡头']
# print(True if 'eva'  in names else False)
# # 输出结果 True 说明 元素'eva' 位于names 列表
names = ['金角大王','黑姑娘','eva','rain','eva','狗蛋','银角大王','鸡头']
print(names[:])  # ['金角大王', '黑姑娘', 'eva', 'rain', 'eva', '狗蛋', '银角大王', '鸡头']
print(names[1::2])  # ['黑姑娘', 'rain', '狗蛋', '鸡头']
print(names[::-1]) # ['鸡头', '银角大王', '狗蛋', 'eva', 'rain', 'eva', '黑姑娘', '金角大王']
print(names[-1:-5:-1]) #  ['鸡头', '银角大王', '狗蛋', 'eva']
print(names[-8:-3]) #  ['金角大王', '黑姑娘', 'eva', 'rain', 'eva']
print(names.sort())