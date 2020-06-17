'''
现有一练习需求，问用户的姓名、年龄、工作、爱好 ，然后打印成以下格式
'''
'''
------------ info of Alex Li -----------
Name  : Alex Li
Age   : 22
job   : Teacher
Hobbie: girl
------------- end -----------------
'''

user_name = input('请输入你的名字：')
user_age = int(input('请输入你的年纪：'))# 将年纪转换为int类型
user_job = input('请输入你的职业：')
user_hobbie = input('请输入你的爱好：')

msg = f'''
------------ info of Alex Li -----------
Name  : {user_name}
Age   : {user_age}
job   : {user_job}
Hobbie: {user_hobbie}
------------- end -----------------
'''
print(msg)