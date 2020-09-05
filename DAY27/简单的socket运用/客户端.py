import socket

# 1，买手机
phone = socket.socket()

# 2，拨号 建立连接 连接服务端的（ip，端口）
phone.connect(('127.0.0.1', 8000))

#3 发送数据 向客户端发数据
phone.send('hello'.encode('utf-8'))

ret = phone.recv(1024)
print(ret, type(ret))
print(ret.decode('utf-8'))