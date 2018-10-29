import socket
import json
import queue
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
				bo = func(ret)




	def server_recv(self):
		ret = self.conn.recv(1024)
		ret_d = json.loads(ret.decode(setting.code))
		return ret_d
	def server_send(self,msg):
		head = json.dumps(msg).encode(setting.code)
		self.conn.send(head)
