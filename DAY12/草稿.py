# 解决选择
# lis = ['find','add','del','update']
# str = 'find'
# if str.startswith('find'):
# 	print('find')
#
# elif str.startswith('add'):
# 	print('add')

# 可以解决查询逻辑
# lis = ['name','age','phone']
# dic = {'1': {'id': '1', 'name': 'Alex Li', 'age': '22', 'phone': '13651054608', 'dept': 'IT', 'date': '2013-04-01'}, '2': {'id': '2', 'name': 'Jack Wang', 'age': '28', 'phone': '13451024608', 'dept': 'HR', 'date': '2015-01-07'}, '3': {'id': '3', 'name': 'Rain Wang', 'age': '21', 'phone': '13451054608', 'dept': 'IT', 'date': '2017-04-01'}, '4': {'id': '4', 'name': 'Mack Qiao', 'age': '44', 'phone': '15653354208', 'dept': 'Sales', 'date': '2016-02-01'}, '5': {'id': '5', 'name': 'Rachel Chen', 'age': '23', 'phone': '13351024606', 'dept': 'IT', 'date': '2013-03-16'}, '6': {'id': '6', 'name': 'Eric Liu', 'age': '19', 'phone': '18531054602', 'dept': 'Marketing', 'date': '2012-12-01'}, '7': {'id': '7', 'name': 'Chao Zhang', 'age': '21', 'phone': '13235324334', 'dept': 'Administration', 'date': '2011-08-08'}, '8': {'id': '8', 'name': 'Kevin Chen', 'age': '22', 'phone': '13151054603', 'dept': 'Sales', 'date': '2013-04-01'}, '9': {'id': '9', 'name': 'Shit Wen', 'age': '20', 'phone': '13351024602', 'dept': 'IT', 'date': '2017-07-03'}, '10': {'id': '10', 'name': 'Shanshan Du', 'age': '26', 'phone': '13698424612', 'dept': 'Operation','date': '2017-07-02'}}
# for v in dic.values():
# 	for i in range(len(lis)):
# 		print(v[lis[i]],end=' ')
		
# lis=['1', 'Alex Li', '22', '13651054608', 'IT', '2013-04-01']
#
# s=' '.join(lis)
# print(s)

# s = input('')
# lis = s.split(' ')
# print(lis)
# lis2 = lis[:]
# for i in lis:
# 	if i == '':
# 		lis2.remove(i)
# print(lis2)
# # print(' '.join(lis2))
# s = ' '.join(lis2)
# print(s)

# s = '>'
# for i in s:
# 	print(i,type(s))
s = '"IT"'
print(s[1:3])
print(s)