
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
	if not user_in.strip():continue
	elif user_in.upper() == 'Q':
		exit()
	elif user_in.upper() == 'B':
		ceng = lis.pop() if len(lis) != 0 else menu
	elif user_in in ceng:
		lis.append(ceng)
		ceng = ceng[user_in]
		if len(ceng) > 0:
			pass
		else:
			ceng = lis.pop()
			print('已经没有数据...即将返回上一级')
	else:
		print('没有此地区.....')