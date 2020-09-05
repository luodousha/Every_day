# 1可以通过类来调用实例方法但是要往实例方法中传递实例对象
# 类型就是类
#比如
lis = []
print(type(lis)) #class list
# 说明lis是类的一个实例化对象
# 相当于数据类型 list 是list 类
#2 数据类型里面的方法都是实例方法可以通过实例化对象调用
lis.append(2) # lis 是list类实例对象
#可以通过如下方法证明
list.append(lis,2)
print(lis)
#输出结果就是[2,2]
