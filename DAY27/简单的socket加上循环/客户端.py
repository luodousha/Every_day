import socket

# 1，买手机
phone = socket.socket()

# 重复利用端口
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  # 可以允许重复使用端口
# 2，拨号 建立连接 连接服务端的（ip，端口）
phone.connect(('127.0.0.1', 8000))

#3 循环发送数据 向客户端发数据
while True:
	user_in = input('>>>：').strip()
	if not user_in: continue # 不允许发送空数据，不然会卡在客户端接收数据阶段
	phone.send(user_in.encode('utf-8'))
	
	ret = phone.recv(1024)
	
	print(ret.decode('utf-8'))

# 关闭客户端
phone.close()