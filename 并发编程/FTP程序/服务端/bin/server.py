import socket
import json
import struct
import os
import hashlib
from threading import Thread,currentThread
import queue
from concurrent.futures import ThreadPoolExecutor
hash = hashlib.md5()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


from bin import import_conf
from bin import storage
socket_air = '%s/conf/socket_conf.ini'%BASE_DIR
info_dir = '%s/conf/userinfo.ini'%BASE_DIR
socket_conf = import_conf.socket_conf(socket_air)
q = queue.Queue(int(socket_conf['queue_size']))
pool = ThreadPoolExecutor(int(socket_conf['submit_size']))
class Server():
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
		super().__init__()

	def __server_bind(self):
		self.socket.bind(self.address)

	def __server_activation(self):
		self.socket.listen(self.request_queue_size)

	def server_close(self):
		self.socket.close()



	def run(self):#程序入口
		while True:
			conn,addr = self.socket.accept()
			q.put(conn)
			pool.submit(self.consumer)



	def consumer(self):
		print(currentThread().getName())
		conn = q.get()
		while True:
			try:
				res = conn.recv(1024)
				if not res: continue
				status = self.landing(res)
				if status['status']:
					head = json.dumps(status).encode(self.coding)
					conn.send(head)

					while True:
						res = conn.recv(4)
						res_len = struct.unpack('i', res)[0]
						head_bytes = conn.recv(res_len)
						head_json = head_bytes.decode(self.coding)
						head_dic = json.loads(head_json)  # {'userinfo': 'jack', 'cmd': 'get', 'filename': '1.txt', 'filesize': 733}
						if hasattr(self, head_dic['cmd']):
							func = getattr(self, head_dic['cmd'])
							func(head_dic,conn)
				else:
					head = json.dumps(status).encode(self.coding)
					conn.send(head)

			except:
				break
	def put(self,args,conn):#上传
		if args['md5'] == hash.update(args['filename'].encode(self.coding)):
			size = 0
			with open('%s/warehouse/%s/%s'%(BASE_DIR,args['userinfo'],args['filename']),'wb') as f:
				res = conn.recv(1024)
				f.write(res)
				size+=len(res)
		else:
			print('两次md5值不一致')
			return


	def get(self,args,conn):#下载
		if args['md5'] == hash.update(args['filename'].encode(self.coding)):
			size = 0
			print(args)
			with open('%s/warehouse/%s/%s'%(BASE_DIR,args['userinfo'],args['filename']),'rb') as f:
				for line in f:
					conn.send(line)
					size+=len(line)
					print(size)
		else:
			print('两次md5值不一致')
			return
	def ls(self,args,conn):#查看服务端用户名下面的文件列表
		lis = os.listdir('%s/warehouse/%s'%(BASE_DIR,args['userinfo']))
		lis_byets = json.dumps(lis).encode(self.coding)
		conn.send(lis_byets)


	def landing(self,data):#登陆函数
		head = data.decode(self.coding)
		head_dic = json.loads(head)
		username = head_dic['username']
		password = head_dic['password']
		info = import_conf.userinfo(info_dir)
		if username in info and password == info[username]['password']:
			return {
				'storage':storage.storage(username),
				'menmory_size':info[username]['menmory_size'],
				'status':True
			}
		else:
			return {"status":False}
