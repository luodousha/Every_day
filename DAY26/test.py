#
#
# def deco(db_type): # 装饰器带参数就是再继续套一层
#    def outer(func):
#       def wrapper(*args,**kwargs):
#          # 这里添加被装饰器前的函数，比如验证
#          user = input('请输入用户名：')
#          pwd = input('请输入密码')
#          if db_type == 'file':
#             print('基于文件验证')
#             if user == 'zzq' and pwd == '123':
#                ret = func(*args,**kwargs)
#                return ret # 假如被装饰函数有返回值
#             else:
#                print('用户名或密码错误....')
#          elif db_type == 'mysql':
#             print('基于mysql验证')
#             ret = func(*args, **kwargs)
#             return ret  # 假如被装饰函数有返回值
#          elif db_type == 'legb':
#             print('基于legb验证')
#             ret = func(*args, **kwargs)
#             return ret  # 假如被装饰函数有返回值
#          else:
#             print('不支持验证类型')
#       return wrapper # 返回wrapper内存地址，偷梁换柱
#    return outer
#
#
# @deco('file')
# def index(a, b):
#    print('欢迎到index页面')
#    print(f'{a},{b}')
#    return a+b
# @deco('mysql')
# def home():
#    print('欢迎进入主页')
# @deco('radies')
# def register():
#    print('欢迎进入注册页面')


#
# lis = ['zzq', 'lw', 'wk']
# for i in enumerate(lis):
#    print(f'编号{i[0]}:学校{i[1]}')
#
# choice = input('请选择学校编号！')
#
# choice = int(choice)
# if choice in range(len(lis)):
#    print(lis[choice])

