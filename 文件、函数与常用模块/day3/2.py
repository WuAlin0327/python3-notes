'''修改个人信息程序
在一个文件里存多个人的个人信息，如以下
alex,abc123,24,Engineer,IT
rain,df2@432,25,Teacher,Teching
jack,123,27,worker,Frame
shanshan,1234,22,model,Pubilc

1.输入用户名密码，正确后登录系统 ，打印
1. 修改个人信息
2. 打印个人信息
3. 修改密码

2.每个选项写一个方法
3.登录时输错3次退出程序
'''
lis = []
info = {}
run = True
count = 0
def modify_info(information):#修改个人信息
	print("-----修改信息页面-----")
	for index,i in enumerate(information):
		print(index,i)
	select = int(input("请选择需要修改信息的编号："))
	print(information[select])
	modify = input("请输入修改后的信息！")
	f = open('info.txt','r+')
	f1 = f.read()
	f1 = f1.replace(information[select],modify)
	f.seek(0)
	f.write(f1)
	f.close()
	information[select] = modify
	print("---修改后信息---")
	for index,i in enumerate(information):
		print(index,i)

while True:


	f = open("info.txt", 'r+')
	file = f.readlines()
	f.close()
	print("重新开始循环")

	for i in file:
		i = i.strip()
		i = i.split(',')
		lis.append(i)
	for index, i in enumerate(lis):
		info[i[0]] = i
	username = input("username>>>")
	password = input("password>>>")
	if username == info[username][0] and password == info[username][1]:
		print("""
	-----welcome-----
	username:	%s
	-------end-------
	""" % (info[username][0]))
	while run:# 主循环
		if username == info[username][0] and password == info[username][1]:

			print("""
	1. 修改信息
	2. 打印个人信息
	3. 修改密码
	""")
			num = int(input("请选择操作："))
			if num == 1:
				lncoming = [info[username][0], info[username][2], info[username][3], info[username][4]]
				modify_info(lncoming)

		else:
			print("登陆失败，请检查用户名与密码是否匹配")
			break

	count += 1
	if count == 3:
		print("登陆次数过多，请稍后再试")
		exit()






