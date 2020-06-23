s = str({'赵志强':['赵志强','123456', 0]})
if '赵志强' in s:
	s = s.replace('0','1')
	
print(s)