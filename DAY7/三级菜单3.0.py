menu = {
	'北京': {
		'海淀': {
			'五道口': {
				'soho': {},
				'网易': {},
				'google': {}
			},
			'中关村': {
				'爱奇艺': {},
				'汽车之家': {},
				'youku': {},
			},
			'上地': {
				'百度': {},
			},
		},
		'昌平': {
			'沙河': {
				'老男孩': {},
				'北航': {},
			},
			'天通苑': {},
			'回龙观': {},
		},
		'朝阳': {},
		'东城': {},
	},
	'上海': {
		'闵行': {
			"人民广场": {
				'炸鸡店': {}
			}
		},
		'闸北': {
			'火车站': {
				'携程': {}
			}
		},
		'浦东': {},
	},
	'山东': {},
}

ceng = menu
lis = []
while True:
	for k in ceng:
		print(k)
	user_in = input('>：')
	if not user_in.strip():
		continue  # 防止用户没有输入内容
	elif user_in.upper() == 'Q':
		print('Bay!')
		exit()  # 退出程序
	elif user_in.upper() == 'B':  # 返回上一级，
		ceng = lis.pop() if len(lis) != 0 else menu  # 输入b or B 取出上一层嵌套字典，赋值
	elif user_in in ceng:
		lis.append(ceng)
		ceng = ceng[user_in]
		if len(ceng) > 0:  # 判断嵌套字典还有没有key
			pass
		else:
			ceng = lis.pop()  # 返回上一级
			print('已经没有数据...即将返回上一级')
	else:
		print('没有此地区.....')
