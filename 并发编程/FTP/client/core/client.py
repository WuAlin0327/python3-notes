import socket
import json
import struct
from conf import setting
class Mylink:
	'''
	与服务器项关联的操作：我的链接
	'''
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
		massage = json.dumps(msg).encode(setting.code)
		self.socket.send(massage)

	def my_recv(self):
		ret = self.socket.recv(1024)
		ret_d = json.loads(ret.decode(setting.code))
		return ret_d

	def send_headler(self,msg):
		'''
		msg:需要发送的数据（字典类型）
			cmd：操作指令
			filename：需要操作的文件对象
			filesize：文件对象的大小
			md5：文件的MD5值，确保文件一致性
		使用struct打包发送给服务端，交给服务端的recv_headler解析出需要的数据
		:param msg:
		:return:
		'''