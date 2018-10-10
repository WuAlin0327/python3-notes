import socket
import json
import struct
import os

BASE_DIR = '/Users/wualin/Documents/python学习笔记/网络编程/day3/文件传输/客户端/download'
print(BASE_DIR)
class Client:
	socket_family = socket.AF_INET #family
	socket_pact = socket.SOCK_STREAM #什么协议
	server_dir = '/Users/wualin/Documents/python学习笔记/网络编程/day3/文件传输/服务端/server'
	coding = 'utf-8'
	max_size = 1024
	def __init__(self,ip_address,conncet=True):
		self.server_address = ip_address
		self.socket = socket.socket(self.socket_family,self.socket_pact)
		if conncet:
			try:
				self.client_conncet()
			except:
				self.client_close()
				raise
	def client_conncet(self):
		self.socket.connect(self.server_address)

	def client_close(self):
		self.socket.close()

	def run(self):
		while True:
			inp = input('>>>:').strip()
			if not inp:continue
			l = inp.split()
			cmd = l[0]
			if len(l) == 1:
				continue
			if hasattr(self,cmd):
				func = getattr(self,cmd)
				func(l)

	def get(self,args):
		cmd = args[0]
		filename = args[1]
		if not os.path.isfile('%s/%s'%(self.server_dir,filename)):
			print('没有找到该文件d:%s'%filename)
			return
		else:
			filesize = os.path.getsize('%s/%s'%(self.server_dir,filename))

		head_dir = {
			'cmd':cmd,
			'filename':os.path.basename(filename),
			'filesize':filesize,
		}
		head_json = json.dumps(head_dir)
		head_bytes = head_json.encode(self.coding)
		head_struct = struct.pack('i',len(head_bytes))
		self.socket.send(head_struct)
		self.socket.send(head_bytes)
		recv_size = 0
		with open('%s/%s'%(BASE_DIR,filename),'wb') as f:
			while recv_size < filesize:
				recv_data = self.socket.recv(1024)
				f.write(recv_data)
				recv_size+=len(recv_data)
				print('文件总大小：%s  已下载：%s'%(filesize,recv_size))




clinet = Client(('127.0.0.1',8256))
clinet.run()
