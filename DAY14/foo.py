__all__ = ['x','change']
print('加载模块foo...')

x = 1


def get():
	print(x)
	return x

def change():
	global x
	x = 100
	return x
if __name__ == '__main__':
    print('aaa')