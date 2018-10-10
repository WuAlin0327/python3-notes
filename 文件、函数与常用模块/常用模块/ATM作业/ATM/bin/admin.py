import os,json,time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from foo import logger
def admin():
	while True:
		print('''
	----- 管理员权限 --- 
	1.txt. 冻结用户
	2. 解冻用户
	3. 添加用户
	4. 删除用户
	5. 用户额度设置
	6. 退出管理员
		''')
		num = input('>>>')
		if num == '1.txt':
			freeze()
		if num == '2':
			no_freeze()
		if num == '3':
			add()
		if num == '4':
			delete()
		if num == '5':
			amount()

		if num == '6':
			break



def freeze():# 冻结用户
	name = input("请输入冻结的用户名：")
	f = open('%s/account/%s.json'%(BASE_DIR,name))
	info = json.load(f)
	f.close()
	info['freeze'] = 1
	f1 = open('%s/account/%s.json'%(BASE_DIR,name),'w')
	json.dump(info,f1)
	f1.close()
	print("该用户已冻结")
	logger.admin_logger("冻结用户%s"%(name))

def no_freeze():# 解冻用户
	name = input("请输入用户名：")
	f = open('%s/account/%s.json'%(BASE_DIR,name))
	info = json.load(f)
	f.close()
	info['freeze'] = 0
	f1 = open('%s/account/%s.json'%(BASE_DIR,name),'w')
	json.dump(info,f1)
	f1.close()
	print("该用户已冻结")
	logger.admin_logger("解冻用户:%s"%(name))

def add():# 添加用户
	data = {}
	data['username'] = input('username:')
	data['password'] = input('password:')
	data['balance'] = int(input('用户余额'))
	data['login_time'] = time.strftime("%Y-%m-%d %X", time.localtime())
	data['status'] = 0
	data['freeze'] = 0
	amount = input('最大额度(输入为空则默认最大额度)：')
	if amount == '':
		data['amount'] = 15000
	else:
		data['amount'] = int(amount)

	f = open('%s/account/%s.json'%(BASE_DIR,data['username']),'w')
	json.dump(data,f)
	f.close()
	print('添加用户成功')
	logger.admin_logger("添加用户:%s"%(data['username']))
def delete():# 删除用户
	del_name = input('请输入需要删除的用户名：')
	os.remove('%s/account/%s.json'%(BASE_DIR,del_name))
	print('删除成功')
	logger.admin_logger('删除用户:%s'%(del_name))

def amount():# 额度设置
	amount_name = input("请输入需要更改额度的用户名:")
	amount_num = int(input("请输入%s的最大额度："%(amount_name)))
	f = open('%s/account/%s.json'%(BASE_DIR,amount_name))
	data = json.load(f)
	f.close()
	data['amount'] = amount_num
	f1 = open('%s/account/%s.json'%(BASE_DIR,amount_name),'w')
	json.dump(data,f1)
	f1.close()
	print("更改成功：%s最大额度为：%s"%(amount_name,amount_num))
	logger.admin_logger("额度设置:%s最大额度为：%s"%(amount_name,amount_num))