import time

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


def func(dic):
	if len(dic) > 0:  # 判断字典里还有没有值
		for n in dic:  # 遍历字典的值
			print(n)
		user_in = input('请输入查询地区>>>:')
		if user_in.upper() == 'Q':
			exit()
		elif user_in.upper() == 'B':
			pass
		if user_in in dic:
			dic = dic.get(user_in)
			func(dic)
		else:
			print('不存在此地区')
	else:
		print('没有数据....,即将退出')
		time.sleep(3)
		return False


while True:
	if func(menu):  # 数据没有见底就一直循环：
		pass
	else:  # 没有数据就退出死循环
		break
