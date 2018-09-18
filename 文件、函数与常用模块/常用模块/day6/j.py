import json
import time
import os
import hashlib
f = open("1234.json",'r+')
f1 = open("1234.json.new",'w')
dic = json.load(f)
count = 0
date = dic['expire_date'].split("-")
time = time.strftime("%Y-%m-%d",time.localtime())
time = time.split("-")

print(date,time)
while count<=2:
	user = input("username:")
	password = input("password:")
	if dic['status'] == 0:
		if user in os.listdir():
			if password == dic['password']:
				if date[0]<=time[0]:
					if date[1] <= time[1]:
						if date[2] < time[2]:
							print("该用户已过期")
				else:
					print("登陆成功")
			else:
				print("密码错误")
				if count == 2:
					dic['status'] = 1
					json.dump(dic,f1)
					os.renames("1234.json.new","1234.json")
					print("该用户已锁定")


	else:
		print("该用户已被锁定")
		break
	count += 1
f.close()
f1.close()