import socket

# 1,买手机
# 第一个参数指基于网络通信，第二个参数是指 字节流类型 的套接字
phone = socket.socket()

# 2, 绑定手机号
phone.bind(('127.0.0.1',8000))  # 以元组形式绑定服务端的ip和端口

# 3, 开机允许挂起5个客户端
phone.listen(5)  # 最多可以挂起5个设备

# 等待客户端打电话(堵塞在此处)
print('等待连接....')
cone, addr = phone.accept()
print(f'{addr}设备已经连接...')
# 循环接收发送数据
while True:
	try:
		ret = cone.recv(1024).decode()  # 1,接收的是bytes类型 2,每次接收最大的数据大小是1024字节
		if not ret: break # linux 上断开客户端会死循环
		ret = ret.upper()
		cone.send(ret.encode())
	except ConnectionResetError: # windows 中处理客户端断开连接的方法
		print(f'客户端{addr}已经断开连接')
		break
# 关闭通道
cone.close()
# 关闭客户端
phone.close()
