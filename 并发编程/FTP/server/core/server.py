import socket
import json
import queue
import struct
import pickle
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from concurrent.futures import ThreadPoolExecutor
from conf import setting
from core import auth


class Server:
	def __init__(self):
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.socket.bind(setting.address)
		self.socket.listen(5)
		self.q = queue.Queue(setting.queue_size)#线程queue大小
		self.pool = ThreadPoolExecutor(setting.thread_size)#线程池大小
		self.auth = auth.Auth()
	def run(self):
		while True:
			self.conn,self.addr = self.socket.accept()
			self.pool.submit(self.deal_with)
	def deal_with(self):
		while True:
			ret = self.server_recv()
			print(ret)
			if hasattr(self.auth, ret['operating']):
				func = getattr(self.auth, ret['operating'])
				res = func(ret)

				self.server_send(res['status'])
				if res['status']:
					self.name = res['username']
					while True:
						user = res['user_obj']
						head = self.recv_head()
						self.q.put(head)
						print(head)
						if hasattr(self,head['cmd']):
							func = getattr(self,head['cmd'])
							func(user)

				else:
					continue






	def server_recv(self):
		ret = self.conn.recv(1024)
		ret_d = json.loads(ret.decode(setting.code))
		return ret_d
	def server_send(self,msg):
		'''
		msg是需要发送的数据
		把需要发送的数据打包成bytes类型发送给客户端
		:param msg:
		:return:
		'''
		head = json.dumps(msg).encode(setting.code)
		self.conn.send(head)

	def recv_head(self):
		'''
		接收并解析报头：
			cmd：操作指令
			filename：需要操作的文件对象
			filesize：文件对象的大小
			md5：文件的MD5值，确保文件一致性
		:return:
		res = conn.recv(4)
		res_len = struct.unpack('i', res)[0]
		head_bytes = conn.recv(res_len)
		'''
		res = self.conn.recv(4)
		head_len = struct.unpack('i',res)[0]
		head_bytes = self.conn.recv(head_len)
		head = json.loads(head_bytes.decode(setting.code))
		head['name'] = self.name
		return head

	def put(self,user):
		head = self.q.get()
		size = 0
		if not os.path.exists('%s/%s'%(user.home,head['filename'])):#判断服务器中是否有该文件，如果有则磁盘覆盖该文件，磁盘空间大小不变
			if user.filesize < user.disk:
				self.server_send(True)
				with open('%s/%s'%(user.home,head['filename']),'wb') as f:
					while size < head['filesize']:
						res = self.conn.recv(1024)
						f.write(res)
						size += len(res)
						user.filesize += len(res)
				with open('%s'%user.file_pick,'wb') as f1:
					pickle.dump(user,f1)

		else:
			self.server_send(True)
			with open('%s/%s'%(user.home,head['filename']),'wb') as f:
				while size < head['filesize']:
					res = self.conn.recv(1024)
					f.write(res)
					size+=len(res)
	def get(self, user):
		head = self.q.get()
		file_dir = '%s/%s'%(user.home,head['filename'])
		if os.path.exists(file_dir):
			filesize = os.path.getsize(file_dir)
			self.server_send(filesize)
			with open(file_dir, 'rb') as f:
				for line in f:
					self.conn.send(line)

		else:
			self.server_send('该文件不存在')

	def ls(self,user):
		lis = os.listdir('%s'%user.home)
		dic = {
			'disk':user.disk,
			'filesize':user.filesize,
			'lis':lis
		}
		self.server_send(dic)
	def cd(self, head):
		pass

	def remove(self,user):
		'''

		:param user:
		:param head: {'cmd': 'remove', 'file': 'miao', 'md5': 2654612354, 'name': 'wualin'}
		:return:
		'''
		head = self.q.get()
		file_dir = '%s/%s'%(user.home,head['filename'])
		file_size = os.path.getsize(file_dir)
		if os.path.exists(file_dir):
			os.remove(file_dir)
			user.filesize -= file_size
			self.server_send(True)
			with open(user.file_pick,'wb') as f:
				pickle.dump(user,f)
		else:
			self.server_send(False)

