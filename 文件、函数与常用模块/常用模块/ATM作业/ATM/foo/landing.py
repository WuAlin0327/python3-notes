import json
import os
BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from . import shopping
def landing(func):
	def inner(username,password):
		f = open('%s/account/%s.json'%(BASE_DIR, username))
		data = json.load(f)
		if username == data['username'] and password == data['password']:
			print("登陆成功")
			func(username,password)

	return inner
@landing
def laned(username,password):
	while True:
		print("""
	----- 欢迎 -----
	1. 查看账户信息
	2. 商城
	3. 取现
	4. 转账
	5. 还款	
		""")

		f = open('%s/account/%s.json'%(BASE_DIR,username))
		data = json.load(f)
		num = input(">>>")
		if num == '1':
			pass
		if num == '2':
			shopping.shopping(data['balance'])
			print(data['balance'])
