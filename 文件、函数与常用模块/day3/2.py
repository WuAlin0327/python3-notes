'''修改个人信息程序
在一个文件里存多个人的个人信息，如以下
alex,abc123,24,Engineer,IT
rain,df2@432,25,Teacher,Teching
jack,123,27,worker,Frame
shanshan,1234,22,model,Pubilc

1.txt.输入用户名密码，正确后登录系统 ，打印
1.txt. 修改个人信息
2. 打印个人信息
3. 修改密码

2.每个选项写一个方法
3.登录时输错3次退出程序
'''
lis = []
info = {}
run = True
count = 0
def open_file(): # 读取文件修改信息后刷新字典
	f = open("info.txt", 'r+')
	file = f.readlines()
	f.close()
	for i in file:
		i = i.strip()
		i = i.split(',')
		lis.append(i)
	for index, i in enumerate(lis):
		info[i[0]] = i
def read_write(old_info,new_info): # 写入文件
	f = open('info.txt','r+')
	f1 = f.read()
	f1 = f1.replace(old_info,new_info)
	f.seek(0)
	f.write(f1)
	f.close()
	print("修改成功")
def modify_info(lncoming):# 修改信息
	'''
	将个人信息列表除了密码之外传入函数参数
	输入需要更改列表的索引
	打开文件并写入更改后的结果
	'''
	print("-----修改信息页面-----")
	print("""
0. username:   %s
1.txt. password:   %s
2. age	   :   %s
3. position:   %s
4. department: %s	
"""%(lncoming[0][0],lncoming[0][1],lncoming[0][2],lncoming[0][3],lncoming[0][4]))
	select = int(input("请选择需要修改信息的编号："))
	if select == 1:
		print("无法修改密码！！")
	else:
		modify = input("请输入修改后的信息：")
		old_info = ','.join(lncoming[0])
		lncoming[0][select] = modify
		new_info = ','.join(lncoming[0])
		read_write(old_info,new_info)
	input("按任意键继续")
def print_info():  # 打印信息
	open_file()
	print("""
-----个人信息-----
username:   %s
age	   :   %s
position:   %s
department: %s	
	""" % (info[username][0],info[username][2],info[username][3],info[username][4]))
	input("按任意键继续")

def modify_password(): # 修改密码
	print("---修改密码页面---")
	old_password = input("old password:")
	new_password = input("new password:")
	if old_password == info[username][1]:
		old_info = ','.join(info[username])
		info[username][1] = new_password
		new_info = ','.join(info[username])
		read_write(old_info,new_info)
	else:
		print("旧密码输入错误")
	input("按任意键继续")
while True: # 登陆循环
	open_file()  #循环打开文件刷新修改后文件中的个人信息
	username = input("username>>>")
	password = input("password>>>")
	if username == info[username][0] and password == info[username][1]:
		print("""
-----welcome-----
	  %s
	""" % (info[username][0]))
		while run: # 主循环
			open_file() #循环打开文件刷新修改后文件中的个人信息
			if username == info[username][0]:

				print("""			
1.txt. 修改信息
2. 打印个人信息
3. 修改密码
4. 退出
		""")
				num = input("请选择操作：")
				if num == '1.txt':
					lncoming = [info[username]]
					modify_info(lncoming)
				if num == '2':
					print_info()
				if num == '3':
					modify_password()
				if num == '4':
					exit()
				else:
					pass

	else:
		print("登陆失败，请检查用户名与密码是否匹配")

	count += 1#最多登陆三次
	if count == 3:
		print("登陆次数过多，请稍后再试")
		exit()






