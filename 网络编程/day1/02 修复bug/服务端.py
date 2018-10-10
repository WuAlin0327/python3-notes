import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1.txt',8082))
s.listen(500)

conn,addr = s.accept()
print(addr)#链接的ip与端口

while True: #通讯循环
	try:
		data = conn.recv(1024)
		if not data:break # 当客户端结束运行时，跳出循环，liunx操作系统
		print('客户端的数据:',data)
		conn.send(data.upper())
	except ConnectionResetError:#使用于当客户端软件运行结束时，监测到客户端软件结束跳出循环
		break

conn.close()
s.close()