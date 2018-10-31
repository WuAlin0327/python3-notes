import socket
import json
import queue
import struct
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
	def monitor(self):
		while True:
			self.conn,self.addr = self.socket.accept()
			ret = self.server_recv()
			if hasattr(self.auth,ret['operating']):
				func = getattr(self.auth,ret['operating'])
				res = func(ret)
				if res:
					self.server_send(res['status'])




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

	def recv_headler(self):
		'''
		接收并解析报头：
			cmd：操作指令
			filename：需要操作的文件对象
			filesize：文件对象的大小
			md5：文件的MD5值，确保文件一致性
		:return:
		'''
		pass
