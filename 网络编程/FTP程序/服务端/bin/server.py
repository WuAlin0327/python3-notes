import socket
import json
import struct
import os
import hashlib

hash = hashlib.md5()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


from bin import import_conf
from bin import storage
socket_air = '%s/conf/socket_conf.ini'%BASE_DIR
info_dir = '%s/conf/userinfo.ini'%BASE_DIR
socket_conf = import_conf.socket_conf(socket_air)

class Server:
	protocol = socket.AF_INET
	trans_type = socket.SOCK_STREAM
	coding = socket_conf['coding']
	request_queue_size = int(socket_conf['request_queue_size'])
	bind_and_activation = True
	def __init__(self,address):
		self.address = address
		self.socket = socket.socket(self.protocol,self.trans_type)
		if self.bind_and_activation:
			self.__server_bind()
			self.__server_activation()


	def __server_bind(self):
		self.socket.bind(self.address)

	def __server_activation(self):
		self.socket.listen(self.request_queue_size)

	def server_close(self):
		self.socket.close()



	def run(self):
		while True:
			self.conn,self.addr = self.socket.accept()
			while True:
				try:
					res = self.conn.recv(1024)
					if not res:continue
					status = self.landing(res)
					print(status['status'])
					if status['status']:
						head = json.dumps(status).encode(self.coding)
						print(head)
						self.conn.send(head)
						while True:
							res = self.conn.recv(4)
							res_len = struct.unpack('i',res)[0]
							head_bytes = self.conn.recv(res_len)
							head_json = head_bytes.decode(self.coding)
							head_dic = json.loads(head_json) #{'userinfo': 'jack', 'cmd': 'get', 'filename': '1.txt', 'filesize': 733}
							if hasattr(self,head_dic['cmd']):
								func = getattr(self,head_dic['cmd'])
								func(head_dic)
					else:
						self.conn.send(str(status).encode(self.coding))

				except:
					break

	def put(self,args):#上传
		if args['md5'] == hash.update(args['filename'].encode(self.coding)):
			size = 0
			with open('%s/warehouse/%s/%s'%(BASE_DIR,args['userinfo'],args['filename']),'wb') as f:
				res = self.conn.recv(1024)
				f.write(res)
				size+=len(res)
		else:
			print('两次md5值不一致')
			return


	def get(self,args):#下载
		if args['md5'] == hash.update(args['filename'].encode(self.coding)):
			size = 0
			print(args)
			with open('%s/warehouse/%s/%s'%(BASE_DIR,args['userinfo'],args['filename']),'rb') as f:
				for line in f:
					self.conn.send(line)
					size+=len(line)
					print(size)
		else:
			print('两次md5值不一致')
			return
	def ls(self,args):#查看服务端用户名下面的文件列表
		lis = os.listdir('%s/warehouse/%s'%(BASE_DIR,args['userinfo']))
		lis_byets = json.dumps(lis).encode(self.coding)
		self.conn.send(lis_byets)


	def landing(self,data):#登陆函数
		head = data.decode(self.coding)
		head_dic = json.loads(head)
		username = head_dic['username']
		password = head_dic['password']
		info = import_conf.userinfo(info_dir)
		if username in info and password == info[username]['password']:
			print('成功')
			return {
				'storage':storage.storage(username),
				'menmory_size':info[username]['menmory_size'],
				'status':True
			}
		else:
			return False
