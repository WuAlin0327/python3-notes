import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',8082))
s.listen(500)

conn,addr = s.accept()
print(addr)#链接的ip与端口

while True: #通讯循环
	data = conn.recv(1024)
	print('客户端的数据:',data)
	conn.send(data.upper())

conn.close()
s.close()