# data = {
#     "name": "alex",
#     "age": 18,
#     "scores": {
#         "语文": 130,
#         "数学": 60,
#         "英语": 98,
#     }
# }
# d2 = data
# data["age"] = 20
# print(d2)

# 浅拷贝
# data = {
#     "name": "alex",
#     "age": 18,
#     "scores": {
#         "语文": 130,
#         "数学": 60,
#         "英语": 98,
#     }
# }
# d2 = data.copy()
# print(id(data), id(d2))
# data["age"] = 20
# print(d2)  #  ---> 18
# print(data)  #  ----> 20

data = {
    "name": "alex",
    "age": 18,
    "scores": {
        "语文": 130,
        "数学": 60,
        "英语": 98,
    }
}
# d2 = data.copy()
# data["age"] = 20
# # data['name'] = '赵志强'
# data["scores"]["数学"] = 77
#
# print(id(d2['age']),id(data['age']))
# print(id(d2['name']),id(data['name']))
# print(id(d2['scores']), id(data['scores']))
# print(d2) # d2 的age地址与 data 的地址是不同 data的年纪会变成20
# d2 还是18
# print(data)
#  数学都是77




# 二分法查找一个数在不在列表中....

# def func(x):
#     if x >= 0:
#         if x % 2 == 0:
#             print(f'{x}是一个偶数')
#         else:
#             print(f'{x}是一个奇数')
#         func(x-1)
#     else:
#         exit()
# func(10)

# a = [1,2,3,4,5,6,7,8,9]
# print(a[3:])
# print(a[:3])
#
# def func(n):
#     print(n)
#     if n > 0:
#         n = int(n/2)
#         func(n)
#     print(n)
# func

# lis = [1,2,3,4]
# print(lis[-2:])
