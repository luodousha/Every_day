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

ceng = menu  # 重新赋值嵌套嵌套字典的变量
count = 0  # 嵌套层数
dic_all = {} # 定义一个字典来保存每层的字典，返回的时候查找字典就行
dic_all[0] = menu  # 第一个字典是menu
while True:  # 死循环
	for k in ceng:
		print(k)
	user_in = input('>')  # 获取用户输入地区
	if not user_in.strip():  # 排除用户输入的空白的情况
		continue
	elif user_in.upper() == 'B':  # 用户输入b/B f返回上一级，将字典重置为上一层
		if count != 0:  # 嵌套次数
			count -= 1
			ceng = dic_all[count]  # {0:menu,1:{'北京'{...}}
		elif count == 0:
			ceng = menu
	elif user_in in ceng:  # 判断是用户输入是否在字典中
		ceng = ceng[user_in]
		if len(ceng) > 0:  # 判断字典中是否还存在元素
			count += 1  # 嵌套层数加1 用来作为key
			dic_all[count] = ceng  #
		elif len(ceng) == 0:
			print('已经没有数据..,即将返回上一级菜单')
			if count != 0:
				count -= 1
				ceng = dic_all[count]   # 当前字典重新赋值为前一个嵌套
			elif count == 0:
				ceng = menu  # 假如嵌套的层数是0 那么字典就是原生menu
	elif user_in.upper() == 'Q':  # 退出
		exit()
	else:
		print('不存在此地址')