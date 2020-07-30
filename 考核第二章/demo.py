import time


def wrapper(func):
	def inter():
		t1 = time.time()
		func()
		t2 = time.time()
		t = t2 - t1
		print(t)
	return inter


@wrapper
def index():
	print('小意思不就是通过考核吗')


index()

# index = wrapper(index)

l = [ x for x in range(1, 11)]


def func(x):
	if x % 2 == 1:
		return True
	else:
		return False

lis = list(filter(func,l))

print(lis)
