import os,sys
import json
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print(BASE_DIR)
from foo import landing

def main():
	ACCOUNT = {}
	while True:
		print('''
	----- 请选择 -----
	1. 注册
	2. 登陆
	
	''')
		num = input(">>>")
		if num == "1": #登陆
			username = input("账号：")
			password = input("密码：")
			balance = input("请输入初始额度：")
			login_time = time.strftime("%Y-%m-%d %X", time.localtime())
			ACCOUNT['username'] = username
			ACCOUNT['password'] = password
			ACCOUNT['balance'] = int(balance)
			ACCOUNT['login_time'] = login_time
			f = open('%s/account/%s.json'%(BASE_DIR,username),'w')
			json.dump(ACCOUNT,f)
			f.close()
			print("注册成功")
		if num == "2": #登陆
			username = input("username:")
			password = input("password:")
			f = open('%s/account/%s.json'%(BASE_DIR,username))
			data = json.load(f)
			landing.laned(username,password,data)


main()

