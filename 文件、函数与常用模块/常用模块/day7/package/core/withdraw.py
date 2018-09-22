import os,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def withdraw(balance,money):
	if balance['balance'] > money:
		balance['balance'] = balance['balance'] - (money - money*0.05)
		print("提现金额：%s,扣除手续费实际到账：%s"%(money,(money-money*0.05)))
		f = open("%s/account/luffy.json"%(BASE_DIR),'w')
		json.dump(balance,f)


