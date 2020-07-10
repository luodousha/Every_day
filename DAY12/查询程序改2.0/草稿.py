


# def func(*args, **kwargs):
# 	def inter(*args, **kwargs):
# 		f = open('staff_table', 'r', encoding='utf-8')
# 		return f
# 	return inter

# def func(mode):
# 	f = open('staff_table', mode, encoding='utf-8')
# 	return f
# a = func('r')
# print(a.read())

def open_file(mode):
	f = open('staff_table',mode,encoding='utf-8')
	return f
f= open_file('r')
print(f.read())