# 交易模块
import os,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from . import logger

def withdraw(data):
	'''
	提现
	:return:
	'''
	wd = input('提现金额：')
	logger.record('提现金额：%s'%(wd))
	if wd.isdigit():
		data['balance'] = data['balance'] - int(wd)-(int(wd)*0.05)
		logger.info('%s已提现金额：%s,扣除手续费：%s,账户余额：%s'%(data['username'],wd,(int(wd)*0.05),data['balance']),data)
		input('>>>')
		f = open('%s/account/%s.json'%(BASE_DIR,data['username']),'w')

		json.dump(data,f)
	else:
		print("转账金额只能是数字!")
		input('>>>')

def transfer(data):
	'''
	转账
	:return:
	'''
	give = input('请输入对方用户名：')
	money = input('请输入转账金额：')
	if money.isdigit():
		if give+'.json' in os.listdir('%s/account'%(BASE_DIR)):
			f = open('%s/account/%s.json'%(BASE_DIR,give))
			give_data = json.load(f)
			f.close()
			if data['balance'] - int(money) <= 0:
				print("你的余额不足，无法进行转账")
			else:
				data['balance'] = data['balance'] - int(money)
				give_data['balance'] = give_data['balance'] + int(money)
				f1 = open('%s/account/%s.json'%(BASE_DIR,data['username']),'w')
				json.dump(data,f1)
				f1.close()
				f2 = open('%s/account/%s.json'%(BASE_DIR,give),'w')
				json.dump(give_data,f2)
				f2.close()
				logger.info('从%s转账到%s，转账金额:%s,你账户内余额：%s'%(data['username'],give_data['username'],money,data['balance']),data)
		else:
			print("账户列表中没有该用户")
	else:
		print("转账金额必须为整数")

def repayment(data):
	'''
	还款
	:return:
	'''
	return_money = input("请输入还款金额：")
	if data['amount'] > int(return_money):
		if return_money.isdigit():
			data['balance'] = data['balance'] + int(return_money)
			logger.info("本次还款金额为：%s,账户内余额为：%s"%(return_money,data['balance']),data)
			f = open('%s/account/%s.json'%(BASE_DIR,data['username']),'w')
			json.dump(data,f)
			f.close()
		else:
			print("还款必须为整数")
	else:
		print("你的最大额度是：%s"%(data['amount']))


