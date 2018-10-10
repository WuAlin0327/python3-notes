import os

BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from . import transaction
from bin import shopping
from . import logger
def landing(func):
	def inner(username,password,data):
		if data['freeze'] == 1:
			print("该用户已被冻结，无法进行登陆，请联系管理员")
		else:
			if data['status'] == 1:
				func(username,password,data)

			elif username == data['username'] and password == data['password']:
				print("登陆成功")
				logger.record('%s成功登陆了ATM'%(username))
				data['status'] = 1
				func(username,password,data)
			else:
				print("账号或者密码错误")
				logger.record('%s尝试登陆ATM'%(username))

	return inner
@landing
def laned(username,password,data):
	while True:
		print("""
	----- 欢迎%s -----
	1.txt. 查看账户信息
	2. 商城
	3. 取现
	4. 转账
	5. 还款	
	6. 退出
		"""%(data['username']))
		num = input(">>>")
		if num == '1.txt':
			logger.record('%s查看了账户信息'%(data['username']))
			for i in data:
				print(i,':',data[i])
			input('>>>')
		if num == '2':
			logger.record('%s进入了商城页面'%(data['username']))
			shopping.shopping(data)
		if num == '3':
			logger.record('%s进入了提现页面'%(data['username']))
			transaction.withdraw(data)
		if num == '4':
			logger.record('%s进入了转账页面'%(data['username']))
			transaction.transfer(data)
		if num == '5':
			logger.record('%s进入了还款页面'%(data['username']))
			transaction.repayment(data)
		if num ==  '6':
			logger.record('%s退出了'%(data['username']))
			break




