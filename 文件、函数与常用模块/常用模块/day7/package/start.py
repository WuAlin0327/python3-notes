import json
import os,sys
from bin import my_log

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from core import wd


def landing(main):
	def inner(money):
		f = open("%s/package/account/user.json"%(BASE_DIR))
		info = json.load(f)
		f.close()
		if info['status'] == 1:
			main(money)
		else:
			while True:
				username = input("username:")
				password = input("password:")
				if username == info['user'] and password == info['password']:
					print("该用户已登陆")

					main(money)
					info['status'] = 1
					f1 = open("%s/account/user.json"%(BASE_DIR),'w')
					json.dump(info,f1)
					f1.close()
				else:
					print("账号或者用户名错误")

	return inner

f = open("%s/package/account/user.json"%(BASE_DIR))
f1 = open("%s/package/account/user.json"%(BASE_DIR))

luffy = json.load(f)
tesla = json.load(f1)
f.close()
f1.close()
@landing
def transfer(money):
	balance = int(luffy['balance'])-money-(money*0.05)
	if balance < 0:
		pass
		#logger.info('用户余额不足')
	else:
		luffy['balance'] = balance
		tesla['balance'] = int(tesla['balance']) + money
		f = open("%s/package/account/user.json"%(BASE_DIR),'w')
		f1 = open("%s/package/account/user.json" % (BASE_DIR), 'w')
		json.dump(luffy,f)
		json.dump(tesla,f1)
		f.close()
		f1.close()

def main():
	print("""
	-----Luffy Bank-----
	1. 账户信息
	2. 转账
	3. 提现
		""")
	while True:
		num = input(">>>")
		if num == '1':
			my_log.info('查询账户余额--账户余额是：%s'%(luffy['balance']))
		elif num == '2':
			money = input("请输入转账金额:")
			transfer(int(money))
		elif num == '3':
			mon = input("请输入提现金额：")
			wd.wd(luffy,int(mon))



main()
