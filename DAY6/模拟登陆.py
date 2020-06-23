'''
练习2
'''
'''
模拟登陆：

用户输入帐号密码进行登陆

用户信息保存在文件内

用户密码输入错误三次后锁定用户，下次再登录，检测到是这个用户也登录不了

'''
#  文件的用户信息保存格式，先不考虑密码加密
# 文件的格式采用字典嵌套列表 lock状态 用 1/0 表示
# {username:[username,password,1/0]} 1：代表被锁定，0：代表没有被锁定

import os

f = open('user_info.txt', 'r', encoding='utf-8')
count = 3
while count > 0:
	user_name = input('请输入用户名：')
	user_password = input('请输入密码：')
	f.seek(0)  # 循环后文件又要从头开始
	line = f.read()
	if line.count(user_name) > 0:  # 判断用户名是否在文件中
		f.seek(0)  # 将光标移到开头
		for line in f:  # 循环取用户的名字
			dic = eval(line.strip())  # 将字符串转换为字典
			user_info = dic.get(user_name)  # 获取字典的value 得到用户的信息
			if user_info is None:  # 用户数据有可能不是存在第一行
				pass
			elif user_info[-1] is 1:  #  如果是1 代表用户是被锁状态
				print('此账号已经被锁定，请联系管理员')
				exit() # 提示后提出
			elif user_info[1] != user_password: # 密码不正确
				print(f'密码错误... {count - 1}次机会')
				if count == 1:
					print('密码输错三次，用户即将被锁定')
					user_info[-1] = 1
					f2 = open('user_info.txt.new', 'w', encoding='utf-8')
					f.seek(0)
					for line in f:
						if user_name in line.strip():
							line = line.replace('0', '1')
						f2.write(line)
					f2.flush()
					f2.close()
					f.close()
					os.replace('user_info.txt.new', 'user_info.txt')
					print('用户已被锁定,即将退出...')
					exit()
			elif user_info[0] == user_name and user_info[1] == user_password:
				print(f'欢迎{user_name}')
				exit()
	# count -= 1
	else:
		print(f'用户名：{user_name} 不存在 ,请重试,{count - 1}次后自动退出')
	count -= 1 # 控制循环
f.close()  # 关闭文件
