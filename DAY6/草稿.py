#  修改存储数据类型
import os
# {'user_name':'password','lock':1/0 }
# 获取用户输入的信息
user_name =input( '请输入用户名:')
user_passwd = input('请输入密码：')
with open('user_info.txt.txt.new',mode='a', encoding='utf-8') as f :
	for line in f:
		print(f.read())