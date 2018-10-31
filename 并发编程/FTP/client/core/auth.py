from core.client import Mylink
from core.transmission import Trans
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class Select(Trans):
	'''
	登陆，注册，退出等操作
	'''
	def __init__(self):
		self.socket = Mylink()

	def laned(self):#注册
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

