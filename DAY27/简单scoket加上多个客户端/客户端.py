import socket

# 创建套接字对象
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 连接服务端
client.connect(('127.0.0.1',8000))

# 循环发送接收消息
while True:
	msg = input('>>>:').strip()
	# 不允许输入空值，会卡住在客户端收数据端口
	if not msg:continue
	# 发送数据
	client.send(msg.encode('utf-8'))
	# 接收服务端发来的数据
	ret = client.recv(1024).decode()
	print(ret)
client.close()
