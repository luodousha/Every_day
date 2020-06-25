'''
可依次选择进入各子菜单
可从任意一层往回退到上一层
可从任意一层退出程序
所需新知识点：列表、字典
'''
import time # 退出太快，引入时间模块看效果
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
while True:
    while True:  # b 返回上一级
        for k in menu:
            print(k)
        user_in = input('>:')
        if not user_in.strip():
            continue  # 判断用户输入，排除用户输入为空的情况
        elif user_in.upper() == 'Q':
            exit()
        elif user_in.upper() == 'B':
            break
        elif user_in in menu:
            dic = menu.get(user_in)  # 第二层的字典
            if len(dic) == 0:
                print('已经没有数据，即将返回上一级')
                time.sleep(1)
                break
            while True:
                for k in menu[user_in]:
                    print(k)
                user_in2 = input('>>:')
                if not user_in2.strip():continue
                elif user_in2.upper() == 'Q':
                    exit()
                elif user_in2.upper() == 'B':
                    break
                elif user_in2 in menu[user_in]:
                    dic = menu[user_in].get(user_in2)  # 第三层字典
                    if len(dic) == 0:  # 判断嵌套字典 还有没有值
                        print('已经没有数据，即将返回上一级')
                        time.sleep(1) # 退出太快了，加一个sleep 看效果
                        break
                   
                    while True:
                        for k in menu[user_in][user_in2]:
                            print(k)
                        # print(dic)
                        user_in3 = input('>>>:')
                        if not user_in3.strip():
                            continue
                        elif user_in3.upper() == 'Q':
                            exit()
                        elif user_in3.upper() == 'B':
                            break
                        elif user_in3 in menu[user_in][user_in2]:
                            dic = menu[user_in][user_in2].get(user_in3)  # 第三层字典
                            if len(dic) == 0:
                                print('已经没有数据，即将返回上一级')
                                time.sleep(1)
                                break
                            
                            while True:
                                for k in menu[user_in][user_in2][user_in3]:
                                    print(k)
                                user_in4 = input('>>>>:')
                                # print(dic)
                                if not user_in4.strip():
                                    continue
                                elif user_in4.upper() == 'Q':
                                    exit()
                                elif user_in4.upper() == 'B':
                                    break
                                elif user_in4 in menu[user_in][user_in2][user_in3]:
                                    dic = menu[user_in][user_in2][user_in3].get(user_in4)  # 第四层字典
                                    if len(dic) == 0:
                                        print('已经没有数据，即将返回上一级')
                                        time.sleep(1)
                                        break
                                else:
                                    print('无此地区..请重试')
                                    continue
                        else:
                            print('无此地区..请重试')
                            continue
                            
                else:
                    print('无此地区..请重试')
                    continue
                    
        else:
            print('无此地区..请重试')
            continue
