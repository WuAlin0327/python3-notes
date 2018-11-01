from core.client import Mylink
from core.transmission import Trans
from conf import setting
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Select(Trans):
	'''
	登陆，注册，退出等操作
	'''
	def __init__(self):
		self.socket = Mylink()

	def laned(self):#登陆
		username = input('username:')
		password = input('password:')
		if username.strip() and password.strip():
			userinfo = {
				'username':username,
				'password':password,
				'operating':'laned'
			}
			self.socket.my_send(userinfo)
			ret = self.socket.my_recv()
			print(ret)
			if ret:
				self.name = username
				print('登陆成功')
				return {
					'status':True,
					'home_dir':'%s/home/%s'%(BASE_DIR,username)
				}
			else:
				return {'status':False}
	def registered(self):#注册
		while True:
			username = input('username:')
			password1 = input('password:')
			password2 = input('password_again:')
			if username.strip() and password1.strip() and password1 == password2:
				userinfo = {
					'username':username,
					'password':password1,
					'operating':'registered'
				}
				self.socket.my_send(userinfo)
				ret = self.socket.my_recv()
				if ret:
					os.mkdir('%s/home/%s'%(BASE_DIR,username))
					self.name = username
					print('注册成功')
					return {
						'status':True,
						'home_dir':'%s/home/%s'%(BASE_DIR,username)
					}
				else:
					print('注册失败')

			else:
				print('请重新输入!')
				continue

	def exit(self):
		exit()

	def get(self,cmd,filename):
		# if not os.path.isfile('%s/home/%s/%s' % (BASE_DIR, self.name, filename)):
		# 	print('没有找到该文件')
		# 	return
		# else:
		dic = {
			'cmd':cmd,
			'filename':filename,
			'md5':555556
		}
		self.socket.send_head(dic)# 发送四个字节的报头
		filesize = self.socket.my_recv()
		if isinstance(filesize,str):
			print(filesize)
			return
		size = 0
		with open('%s/home/%s/%s'%(BASE_DIR,self.name,filename),'wb') as f:
			while filesize > size:
				ret = self.socket.socket.recv(1024)
				f.write(ret)
				size += len(ret)
				progress = int((size / filesize) * 100)
				pro = int(progress / 10)
				print('正在下载中：%s' % (progress), '%', '=' * pro)

	def put(self,cmd,filename):
		print(cmd,filename)

	def ls(self,cmd,filename):
		pass

	def cd(self,cmd,filename):
		pass

