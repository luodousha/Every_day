# import foo
# #
# print(foo.x)
# print(foo.get())
# print(foo.change())


# from foo import x
#
# from foo import get
#
# from foo import change

x = 10000
# print(foo.x)
# print(locals())
# print(x)
# change()
# print(x)

# print(__name__)

from foo import *  # 这里导入的时候重新对x 进行了赋值
print(x)
# print(get())
print(change()) #  调用change()返回x
# from foo import x # 假如再导入一遍就会重新对x 重新赋值
print(x)