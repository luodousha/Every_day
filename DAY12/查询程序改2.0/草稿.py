


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

# def open_file(mode):
# 	f = open('staff_table',mode,encoding='utf-8')
# 	return f
# f= open_file('r')
# print(f.read())

# s = '6,Eric Liu,19,18531054602,Marketing,2012-12-01'
# if 'IT' in s:
# 	print('hh')
def func(old_str,new_str):
	f = open('staff_table', 'r')
	f2 =open('staff_table_new_jj', 'w')
	for line in f:
		if old_str in line:
			line=line.replace(old_str,new_str)
		f2.write(line)
	f2.close()
	f.close()
	
	
func('IT','Market')