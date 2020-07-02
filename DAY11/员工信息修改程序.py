def login():
    # dic = {}  # 用来存储，用户的信息
    # with open('user_info.txt.txt','r') as f:
    # 	column = f.readline()
    #
    
    
    print('员工信息修改程序接口')
    user_name = input('请输入用户名:')
    user_password = input('请输入密码：')

def register():
    pass

def change_personal_info():
    '''
    修改用户信息
    :return:
    '''
    pass

def read_data():
	dic = {}
	with open('user_info', 'r', encoding='utf-8') as f:
		column = f.readline().strip().split(',')  # 得到行首
		for line in f.readlines():
			line = line.strip().split(',')
			print(line)
			dic.setdefault(line[0], {x: y for x, y in zip(column, line)})
		# print(dic)
	return dic
def run():
    print('欢迎使用员工信息修改程序v1.0'.center(58,'-'))
    print('程序说明'.center(66,'-'))
    print('1:登录')
    print('2:注册')
    print('3:退出')
    user_in = input()
    if not user_in.strip():
        print('用户输入不能为空!')
    if not user_in.isdigit():
        print('请选择数字‘1’或‘2’')
        exit()
    if int(user_in) == 1:
        login()
    elif int(user_in) == 2:
        register()
    else:
        print('选择功能错误请重试!')

if __name__ == '__main__':
	pass
    

        