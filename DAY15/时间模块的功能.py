import time   # 导入内置的模块time

# print(t)

# print(time.localtime())
#
# print(time.gmtime(t))
t = time.localtime()
print(t)
print(time.strftime('%Y-%m-%d %H:%M:%S',t))

t = time.strptime('2020-6-28','%Y-%m-%d')
print(t)