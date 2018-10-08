import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#重复使用端口，解决端口被占用问题


s.connect(('127.0.0.1',8082))

while True:
	msg = input('发送信息：')
	if not msg:continue#发送数据不能为空
	s.send(msg.encode('utf-8'))
	data = s.recv(1024)
	print('接收消息',data.decode('utf-8'))

s.close()