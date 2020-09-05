import socket

# 1,买手机
# 第一个参数指基于网络通信，第二个参数是指 字节流类型 的套接字
phone = socket.socket()

# 2, 绑定手机号
phone.bind(('127.0.0.1',8000))  # 以元组形式绑定服务端的ip和端口

# 3, 开机
phone.listen(5)  # 最多可以挂起5个设备

# 等待客户端打电话(堵塞在此处)
print('等待连接....')
cone, addr = phone.accept()
print(f'{addr}设备已经连接...')
# 接收数据
ret = cone.recv(1024)  # 1,接收的是bytes类型 2,每次接收最大的数据大小是1024字节
print(ret,type(ret))
cone.send('hh'.encode('utf-8'))

# 关闭通道
cone.close()


# 关闭客户端
phone.close()
