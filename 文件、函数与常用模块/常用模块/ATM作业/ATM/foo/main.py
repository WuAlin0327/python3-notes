import os,sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print(BASE_DIR)
from foo import landing
from bin import admin
def main():
	ACCOUNT = {}
	while True:
		print('''
	----- 请选择 -----
	1.txt. 用户登陆
	2. 管理员登陆
	3. 退出
	
	''')
		num = input(">>>")

		if num == "1.txt": #登陆
			username = input("username:")
			password = input("password:")
			f = open('%s/account/%s.json'%(BASE_DIR,username))
			data = json.load(f)
			landing.laned(username,password,data)
		if num == "2": #登陆
			username = input("账号：")
			password = input("密码：")
			if username == 'admin' and password == 'admin':
				admin.admin()
			else:
				print('管理员账号或者密码错误')
		if num == '3':#退出
			return


main()

