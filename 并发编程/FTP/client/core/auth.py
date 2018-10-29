from core.client_link import Mylink
class Select:
	'''
	登陆，注册，退出等操作
	'''
	def __init__(self):
		self.socket = Mylink()

	def laned(self):
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

	def registered(self):
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
				print('注册成功')
				break
			else:
				print('请重新输入!')
				continue

	def exit(self):
		pass


