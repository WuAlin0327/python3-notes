from core.client import Mylink
from conf import setting
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Select():
	'''
	登陆，注册，退出等操作
	'''
	def __init__(self):
		self.socket = Mylink()

	def laned(self):#登陆
		print('登陆')
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
			if ret:
				self.name = username
				print('Wecome %s'%username)
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
					print('该用户已存在')

			else:
				print('请重新输入!')
				continue

	def quit(self):
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
		file_dir = '%s/home/%s/%s' % (BASE_DIR, self.name, filename)
		if os.path.exists(file_dir):
			file_dir = '%s/home/%s/%s' % (BASE_DIR,self.name,filename)
			filesize = os.path.getsize(file_dir)
			dic = {
				'cmd':cmd,
				'filename':filename,
				'filesize':filesize,
				'md5':2321315
			}
			self.socket.send_head(dic)
			res = self.socket.my_recv()
			size = 0
			if res:
				with open(file_dir,'rb') as f:
					for line in f:
						self.socket.socket.send(line)
						size += len(line)
						progress = int((size / filesize) * 100)
						pro = int(progress / 10)
						print('正在上传中：%s' % (progress), '%', '=' * pro)
			else:
				print('磁盘空间不足')
		else:
			print('该文件不存在')

	def ls(self,cmd,filename=None):
		dic = {
			'cmd':cmd,
		}
		self.socket.send_head(dic)
		res = self.socket.my_recv()
		print('''
磁盘总大小：%s
已用磁盘空间：%s
剩余磁盘空间：%.2f %s
		'''%(res['disk'],res['filesize'],(res['filesize']/res['disk'])*100,'%'))
		for index,i in enumerate(res['lis'],1):
			print(index,'.',i)

	def cd(self,cmd,filename):
		pass

	def remove(self,cmd,filename):
		dic = {
			'cmd':cmd,
			'filename':filename,
			'md5':2654612354
		}
		self.socket.send_head(dic)
		res = self.socket.my_recv()
		if res:
			print('删除成功')
		else:
			print('没有找到该文件')

	def exit(self,cmd,filename):
		self.socket.socket.close()
		exit()
