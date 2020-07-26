
def login():
	print('登录功能')
	
	
def register():
	print('注册功能')

	
def transfer():
	print('转账功能')


def withdraw():
	print('提现')
	

select_func = {
	0: ['退出', exit],
	1: ['登录', login],
	2: ['注册', register],
	3: ['提现', withdraw],
	4: ['转账', transfer]
}


def run():
	for k in select_func:
		print(k,select_func[k][0])
	user_in = int(input('请选择程序'))
	select_func.get(user_in)[1]()