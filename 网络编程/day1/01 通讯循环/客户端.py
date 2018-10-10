import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1.txt',8082))

while True:
	msg = input('发送信息：')
	s.send(msg.encode('utf-8'))
	data = s.recv(1024)
	print('接收消息',data)

s.close()