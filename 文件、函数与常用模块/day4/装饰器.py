status = False

def login(func):
	def inner():
		username = 'jack'
		password = '123'
		global status
		_username = input('username:')
		_password = input('password:')
		if status == False:
			if _username == username and _password == password:
				print('登陆成功')
				status = True
			else:
				print('登陆失败')
		else:
			print("用户已登陆")
		if status:
			func() #henan
	return inner
@login #henan = login(henan)
def henan():
	print("---河南---")

def jiangxi():
	print("---江西---")

def guangdong():
	print("---广东---")

# henan = login(henan)  变量henan相当于inner的内存地址