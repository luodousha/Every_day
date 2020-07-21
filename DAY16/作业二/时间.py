import time
# import re
'''
一月:Jan.

二月:Feb.

三月：Mar.

四月：Apr.

五月：May.

六月：Jun.

七月：Jul.

八月：Aug.

九月：Sept.

十月：Oct.

十一月：Nov. 

十二月：Dec
'''
import re
str_ = '15/Apr/2019:00:00:04 +0800'
def func(str_):
	'''
	月份转换
	:return:
	'''
	month_dic = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sept': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
	result = re.findall(r'[A-Za-z]{3,}', str_)
	print(result[0])
	if month_dic.get(result[0]):
		str_ = str_.replace(result[0],str(month_dic.get(result[0])))
	print(str_)
	return str_
s = func(str_)
print(s)
s = s[:-6]
print(s)
t=time.strptime(s,'%d/%m/%Y:%H:%M:%S')
print(t)
# tt = time.altzone
# print(tt)