'''

'''
'''
针对列表
names=[‘金角大王’, ‘黑姑娘’, ‘rain’, ‘eva’, ‘狗蛋’, ‘银角大王’, ‘eva’,’鸡头’]进入以下操作

通过names.index()的方法返回第2个eva的索引值

把以上的列表通过切片的形式实现反转

打印列表中所有下标为奇数的值

通过names.index()方法找到第2个eva值 ，并将其改成EVA

'''
names = ['金角大王', '黑姑娘', 'rain', 'eva','狗蛋', '银角大王', 'eva', '鸡头']
# 要求 1 通过names.index()的方法返回第2个eva的索引值
first=names.index('eva')  # 看一看第一个'eva'的索引
print(names.index('eva', first+1, len(names)))
# 输出结果是6

# 要求 2 切片形式反转列表
print(names[::-1])
# 输出结果 ['鸡头', 'eva', '银角大王', '狗蛋', 'eva', 'rain', '黑姑娘', '金角大王']

# 要求 3 打印列表中所有下标为奇数的值
print(names[1::2])
# 输出结果 ['黑姑娘', 'eva', '银角大王', '鸡头']

# 要求 4
names[names.index('eva', first+1, len(names))] = 'EVA'
print(names)
#  输出结果 ['金角大王', '黑姑娘', 'rain', 'eva', '狗蛋', '银角大王', 'EVA', '鸡头']
