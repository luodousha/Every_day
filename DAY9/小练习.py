#  1.根据下图所示，对print_info里的代码进行实现
# def print_info(*args,**kwargs):
# 		print('-----user_info------')
# 		kwargs['hobbie'] = '大保健'
# 		msg = f'''Name:{kwargs['name']}
# Age :{kwargs['age']}
# Sex :{kwargs['sex']}
# Hobbie:{kwargs['hobbie']}
# 		'''
# 		print(msg.strip())
# print_info(name='Alex',age = 20 ,sex = 'M')
# print_info(name='Jack', age = 26, sex = 'M', hobbie = '学习')

# name = "小猿圈"
# def change():
#     name = "小猿圈，自学编程"
#     def change2():
#         # global name  如果声明了这句，下面的name改的是最外层的全局变层
#         name = "小猿圈，自学编程不要钱" #这句注释掉的话，下面name打印的是哪个值？
#         print("第3层打印", name)
#     change2()  # 调用内层函数
#     print("第2层打印", name)
# change()
# print("最外层打印", name)


# def outer():
# 	a = 100  # 局部变量a可以在outer函数中随意使用，外部却不能访问，变量a
#
# 	def inter():
# 		print(a)  # 这里一定要用到a变量
# 	inter()
# 	return inter
#
# 	def inter2():
# 		print(a)  # 局部变量a在outer函数中可以随意使用
# ret = outer()  # 这里用一个全局变量指向了inter函数的内存地址，常驻内存
# ret()
