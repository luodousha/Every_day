# 集合的作用
# 一 去重
# 关系运算

# 集合特性
# 集合是不可变类型，天生去重，里面的值唯一，无序，{3,4,5}和{3,5,4}是同一个集合
# 1：可以用来列表的去重
# 2：可以用来关系运算 集合间的
s = {1,2,3,4,6,7}
# 集合的增删改查
# 增：
# ① add() 增加
s.add(7) # 添加值，假如添加的值已有不会报错
print(s)
s.add(10) # 没有此值就会增加
print(s)
# ② update()
print(s)
s.update([1,12,28]) # 将可迭代对象依次添加到 s 集合中 会除掉重复的值
print(s)

# 删：
# ①del s
# del s # 整个清除
print(s)

# ② discard（）
s.discard('sdsdsd') #删掉集合中的元素 ，假如没有次元素成员，不会报错
print(s)

# ③ clear（）清空
# s.clear()
print(type(s)) # 清空

# ④ pop()
# 因为集合是无序的，所以pop（）是随机删除
# s.pop()
print(s)

# ⑤ remove()
# 移除某元素，如果没有此成员，会报错
s.add('zzq')
s.add('xcc')
s.remove('zzq')
print(s)

# 改
# 不支持修改

# 查
print(s)
# 用关键子 in
print( 2 in s ) # 返回True 说明2 在集合中


s_1024 = {"佩奇","老男孩","海峰","马JJ","老村长","黑姑娘","Alex"}
s_pornhub = {"Alex","Egon","Rain","马JJ","Nick","Jack"}

# 两个集合的交集
new_s = s_1024 & s_pornhub
print(new_s) # 逛草榴社区，还逛黄网的淫魔

# 两个集合的合集
new_s = s_1024 | s_pornhub # 只要逛不良网站的都是不良少年啊
print(new_s)

# 差集
new_s = s_1024 - s_pornhub
print(new_s) # 只逛1024的人

new_s = s_pornhub - s_1024
print(new_s) # 只逛 porthub的人

# 将交集的去掉 对称差集 都看的人踢掉

new_s = s_1024 ^ s_pornhub
print(new_s) # 去掉了‘Alex’ 和 ‘马JJ’

# 集合之间的关系
# 1 包含
print(s_1024.isdisjoint(s_pornhub))     # 判断2个集合是不是不相交，返回True or False

# 2 相交
print(s_1024.issubset(s_pornhub))       # 判断s_1024是不是s_pornhub的子集，返回True or False

# 3 不相交
print(s_1024.issuperset(s_pornhub))     # 判断s_1024是不是s_pornhub的父集，返回True or False