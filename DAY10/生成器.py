## 列表推导式
# lis = [x for x in range(10)]

# 生成式推导式
# 生成器就是保留了一个算法，等到需要的时候把值取出来
# g = (x +1 for x in range(10))
# print(next(g))
# print('我要吃饭')
# print(next(g))
# print('我又要拉屎')
# print(next(g))
# for i in g :
# 	print(i)
# print(g)
# print(next(g)) # 当g里面没有值了就会报错，

# 斐波那契数列
# [1,1,2,3,5,8,12,......]
# def func(n):
# 	count = 0
# 	a,b = 0, 1
# 	if b == 1:
# 		print(b)
# 	while count < n:
# 		tem = a
# 		a = b
# 		b = tem + b
# 		print(b)
# 		count += 1
# func(12)

# def func(n):
# 	count = 0
# 	a,b = 0, 1
# 	if b == 1:
# 		print(b)
# 	while count < n:
# 		tem = a
# 		a = b
# 		b = tem + b
# 		count += 1
# 		yield b
#
# f = func(10)


import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield  # yield可以接收到外部send传过来的数据并赋值给baozi
       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
c = consumer('A')
c2 = consumer('B')
c.__next__() # 执行一下next可以使上面的函数走到yield那句。 这样后面的send语法才能生效
c2.__next__()

for i in range(10):
	time.sleep(1)
	c.send(i)
	c2.send(i)







# print("----老子开始准备做包子啦!----")
# for i in range(10):
#     time.sleep(1)
#     print("做了2个包子!")
#     c.send(i)  # send的作用=next, 同时还把数据传给了上面函数里的yield
#     c2.send(i)
