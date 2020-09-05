import socket

# 创键套接字对象
#创键基于tcp协议的套接字
sever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 重复使用端口
sever.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# 绑定端口
sever.bind(('127.0.0.1',8000))

# 设置监听个数
sever.listen(5)

# 挂起等待连接
while True:
	# 建立连接通道 conn 也是一个套接字
	conn,client_addr = sever.accept()
	print(f'客户端{client_addr}已经连接...')
	# 循环接发消息
	while True:
		# 1 接收的数据都是字节流bytes类型，2 每次允许接收的数据最大是1024字节
		try:
			date = conn.recv(1024).decode()
			# linux 上解决 客户端突然断开，服务端陷入死循环的bug 情况
			if not date:break
			
			# 将客户端传过来的字母变成大写后发送给客户端
			msg = date.upper()
			# 发送数据bytes 类型
			conn.send(msg.encode())
		# 解决windows 上 客户端断开的 bug
		except ConnectionResetError:
			print(f'客户端{client_addr}已经断开...')
			break
	# 关闭连接通道
	conn.close()

# 关闭服务端
sever.close()


