import socket
import json
import struct
import os
import hashlib

hash = hashlib.md5()
mb = 1048576

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
server_dir = '%s/服务端/warehouse'%os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Client:
	protocol = socket.AF_INET
	trans_type = socket.SOCK_STREAM
	coding = 'utf-8'
	conn = True
	def __init__(self,address):
		self.address = address
		self.socket = socket.socket(self.protocol,self.trans_type)
		if self.conn:
			self.client_conn()
		else:
			pass

	def client_conn(self):
		self.socket.connect(self.address)

	def exit(self,args):
		self.socket.close()
		exit()
	def run(self):
		while True:
			head = self.landing()
			self.socket.send(head)
			res = self.socket.recv(1024).decode(self.coding)
			print(res)
			self.res_dic = json.loads(res)
			if self.res_dic['status']:
				while True:
					inp = input('>>>:')
					if not inp:continue
					l = inp.split()
					cmd = l[0]
					if hasattr(self,cmd):
						func = getattr(self,cmd)
						func(l)
			else:
				print('账号或者密码错误')
	def put(self,args):#从本地上传到服务端文件
		if self.res_dic['storage']/mb < int(self.res_dic['menmory_size']):
			cmd = args[0]
			filename = args[1]
			size = 0
			if not os.path.isfile('%s/folder/%s/%s'%(BASE_DIR,self.name,filename)):
				print('没有找到该文件')
				return
			else:
				filesize = os.path.getsize('%s/folder/%s/%s'%(BASE_DIR,self.name,filename))
			head = {
				'userinfo':self.name,
				'cmd':cmd,
				'filename':filename,
				'filesize':filesize,
				'md5':hash.update(filename.encode(self.coding))
			}
			head_bytes = json.dumps(head).encode(self.coding)
			head_len = struct.pack('i',len(head_bytes))
			self.socket.send(head_len)
			self.socket.send(head_bytes)

			with open('%s/folder/%s/%s'%(BASE_DIR,self.name,filename),'rb') as f:
				for line in f:
					self.socket.send(line)
					size+=len(line)
					progress = int((size/filesize)*100)
					bar = int(progress/10)
					print('正在上传：%s'%(progress),'%','='*(bar))
		else:
			print('储存空间不足')




	def get(self,args):#下载文件
		cmd = args[0]
		filename = args[1]
		if not os.path.isfile('%s/%s/%s'%(server_dir,self.name,filename)):
			print('没有找到该文件')
			return
		else:
			filesize = os.path.getsize('%s/%s/%s'%(server_dir,self.name,filename))
		head = {
			'userinfo':self.name,
			'cmd':cmd,
			'filename':filename,
			'filesize':filesize,
			'md5':hash.update(filename.encode(self.coding))
		}#报头
		head_bytes = json.dumps(head).encode(self.coding)
		head_len = struct.pack('i',len(head_bytes))
		self.socket.send(head_len)
		self.socket.send(head_bytes)
		size = 0
		with open('%s/folder/%s/download/%s' % (BASE_DIR, self.name, filename), 'wb') as f:
			while size < filesize:

				res = self.socket.recv(1024)
				f.write(res)
				size+=len(res)
				progress = int((size/filesize)*100)
				pro = int(progress/10)
				print('正在下载中：%s'%(progress),'%','='*pro)

	def landing(self):#登陆
		username = input('username:')
		password = input('password:')
		info = {
			'username':username,
			'password':password
		}
		self.name = username
		return json.dumps(info).encode(self.coding)
	def ls(self,args): #查看当前文件夹下的列表
		print('总储存空间:%smb 已用:%.4fmb'%(self.res_dic['menmory_size'],self.res_dic['storage']/mb))#打印储存空间和生育储存空间
		cmd = args[0]
		head = {
			'userinfo':self.name,
			'cmd':cmd
		}

		head_byest = json.dumps(head).encode(self.coding)
		head_len = struct.pack('i',len(head_byest))
		self.socket.send(head_len)
		self.socket.send(head_byest)
		res = self.socket.recv(1024).decode(self.coding)
		res_data = json.loads(res)
		for i in res_data:
			print(i)
	def cd(self):
		pass



