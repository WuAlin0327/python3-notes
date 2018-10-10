import socket
import json
import struct
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Server:
	socket_family = socket.AF_INET #family
	socket_pact = socket.SOCK_STREAM #什么协议
	repeat_address = False #重用ip
	request_queue_size = 5 #最大连接数
	server_dir = '/Users/wualin/Documents/python学习笔记/网络编程/day3/文件传输/服务端/server'
	coding = 'utf-8'
	max_packet_size = 1024
	def __init__(self,ip_address,bind_and_activate=True):
		self.ip_address = ip_address
		self.socket = socket.socket(self.socket_family,self.socket_pact)
		if bind_and_activate:#判断是否绑定与激活默认是绑定并且激活
			try:
				self.server_bind()
				self.server_activate()
			except:
				pass


	def server_bind(self):
		if self.repeat_address:
			self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.socket.bind(self.ip_address)

	def server_activate(self):
		self.socket.listen(self.request_queue_size)

	def server_close(self):
		self.socket.close()

	def get_request(self):
		return self.socket.accept()

	def run(self):
		while True:
			self.conn,self.client_addr = self.get_request()
			while True:
				try:
					head = self.conn.recv(4)
					if not head:continue
					head_len = struct.unpack('i',head)[0]
					print(head_len)
					head_byest = self.conn.recv(head_len).decode(self.coding)
					head_dic = json.loads(head_byest)
					cmd = head_dic['cmd']
					if hasattr(self,cmd):
						func = getattr(self,cmd)
						func(head_dic)

				except:
					break

	def get(self,aggr):
		send_size = 0
		with open('%s/server/%s'%(BASE_DIR,aggr['filename']),'rb') as f:
			for line in f:
				self.conn.send(line)
				send_size+=len(line)
				print(send_size)


	def put(self):
		pass

server = Server(('127.0.0.1',8356))
server.run()
