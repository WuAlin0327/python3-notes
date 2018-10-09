import socket
import subprocess
import struct
import json

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',8022))
s.listen(500)
while True:#链接循环
	conn,addr = s.accept()
	print(addr)#链接的ip与端口

	while True: #通讯循环
		try:
			#接收命令
			cmd = conn.recv(1024)
			if not cmd:break # 当客户端结束运行时，跳出循环，liunx操作系统
			obj = subprocess.Popen(cmd.decode('utf-8'),shell=True,
								   stdout=subprocess.PIPE,
								   stderr=subprocess.PIPE)
			stdout = obj.stdout.read()
			stderr = obj.stderr.read()
			#把命令返回

			#1.制作固定长度报头
			header_dic = {
				'filename':'xxx',
				'md5':'423123wdw',
				'recv_size':len(stderr)+len(stdout)
			}
			header_json = json.dumps(header_dic)
			header_b = header_json.encode('utf-8')

			header = struct.pack('i',len(header_b))
			#2.发送报头
			conn.send(header)
			conn.send(header_b)
			#3.发送真实数据
			conn.send(stdout)
			conn.send(stderr)
		except ConnectionResetError:#使用于当客户端软件运行结束时，监测到客户端软件结束跳出循环
			break

	conn.close()
s.close()