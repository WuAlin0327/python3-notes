import socket
import json
from conf import setting
class Mylink:

	__instance = None
	def __init__(self):
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.socket.connect(setting.addr)

	def __new__(cls, *args, **kwargs):
		if not cls.__instance:
			obj = object.__new__(cls)
			cls.__instance = obj
		return cls.__instance


	def my_send(self,msg):
		print('my_send')
		massage = json.dumps(msg).encode(setting.code)
		self.socket.send(massage)

	def my_recv(self):
		ret = self.socket.recv(1024)
		ret_d = json.loads(ret.decode(setting.code))
		return ret_d
