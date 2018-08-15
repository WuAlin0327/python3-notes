'''
_user = "seven"
_password = 123

user = input("请输入用户名：")
password = int(input("请输入密码："))

if _user == user and _password == password:
	print("登陆成功")
else:
	print("登陆失败")
'''
'''
_user = "seven"
_password = 123

count = 0
while count<= 2:
	user = input("请输入用户名：")
	password = int(input("请输入密码："))

	if _user == user and _password == password:
		print("登陆成功")
	else:
		print("登陆失败")
	count+=1
'''
'''
_user = "seven" and "alex"
_password = 123

count = 0
while count<= 2:
	user = input("请输入用户名：")
	password = int(input("请输入密码："))

	if _user == user and _password == password:
		print("登陆成功")
		break
	else:
		print("登陆失败")
	count+=1
'''