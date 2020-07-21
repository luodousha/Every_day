'''
pv:page visit , 页面访问量，一次请求就是一次pv
uv: user visit, 独立用户，一个ip就算一个独立用户
1 统计本日志文件的总pv、uv
2 列出全天每小时的pv、uv数
3 列出top 10 uv的IP地址，以及每个ip的pv点击数
4 列出top 10 访问量最多的页面及每个页面的访问量
5 列出访问来源的设备列表及每个设备的访问量
'''

# import re
#
# regex = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\[(.*?)\s\+.*].*?\/(.*?)\s.*?http.*?\s\"(.*?\))"
# lis = []
# def read_data_file():
# 	f = open('网站访问日志（utf-8）.txt','r',encoding='utf-8')
# 	f2 = open('gg', 'w', encoding='utf-8')
# 	for line in f.readlines():
# 		# count += 1  # 测试有多少行 --> 32162
# 		r = re.compile(regex)
#
# read_data_file()
def func():
	count = 0
	f = open('网站访问日志（utf-8）.txt', 'r', encoding='utf-8')
	f2 = open('gg','w', encoding='utf-8')
	for line in f.readlines():
		count += 1
		if count <= 100:
			f2.write(line)
			# count += 1
func()