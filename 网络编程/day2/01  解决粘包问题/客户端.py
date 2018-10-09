import socket
import struct
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#重复使用端口，解决端口被占用问题


s.connect(('127.0.0.1',8084))



while True:
	#发命令
	cmd = input('>>>')
	if not cmd:continue#
	s.send(cmd.encode('utf-8'))
	# 接收报头
	hadere = s.recv(4)
	recv_len = struct.unpack('i',hadere)[0]

	recv_1 = 0
	res = b''
	while recv_1 < recv_len:
		#拿到命令的结果
		data = s.recv(1024)
		recv_1+=len(data)
		res+=data


	print('接收消息',res.decode('utf-8'))


s.close()