# 字符串居中
# center()
my_name = 'ZZLQnQLg'
print(my_name.center(50,'-'))
#  -----------------------ZZQ------------------------
#输出结果，将字符串居中，总长度50,其余用后面的格式填充

# index()
# 查找元素索引
# 默认查找字符串的元素，显示查到的第一个,找不到就报错
# 可以给定start,和end 返回找到字符串元素的索引，找不到就报错
print(my_name.index('L',3,-1))

# count()
#  统计计数
print(my_name.count('Q'))
# 同样也是可以指定开始和结束，在这个区间出现元素的次数

# isdigit()
# 判断字符串是否是有数字组成的字符串
print(my_name.isdigit())
print('1.234'.isdigit())# 判断是否由整型数字组成的字符串
print('21313'.isdigit())

# upper()
# 将字符串全部变成大写
print(my_name.upper())

# strip()
# 去除两边的空白也会去除\n \t ,\n \t 本质上也是空白
print(len(my_name))
my_name.strip()
print(len(my_name.strip())) # 输出的长度是7 已经去掉空白

# find()
print(my_name.find('s'))
# 基本与index 类似 ，不同的是找不到的时候会返回-1

# split()
# 以某某元素为界 由左向右分割字符串，假如切割的元素找不到，就会返回一个带字符串的列表
print(my_name.split('Q',-1))
# 默认会全部切割，后面可以设置切多少次

#由右向左切割
print(my_name.rsplit('Q',))

# join()
# 连接
print('*'.join(my_name))


# replace()
# 从右向左替换代替将A元素替换成B ，默认是全部替换，可以设置count来改变修改的次数
# my_name.replace()
print(my_name.replace('Q','JJ',1))

#format()
# 格式
