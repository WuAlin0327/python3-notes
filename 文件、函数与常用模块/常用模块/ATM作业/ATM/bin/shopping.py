import json,os
import configparser
from foo import landing
from foo import logger


BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def shopping(data):#购物车
	shopping_cart = []
	config = configparser.ConfigParser()
	config.read('%s/conf/commodity.ini'%(BASE_DIR))
	commodity = config['COMMODITY']
	print("--- 商品列表 ---")
	for i in commodity:
		print(i,commodity[i])
	while True:
		res_name = input("请输入商品名称：")
		logger.record('输入商品名称：%s'%(res_name))
		money = []
		if data['balance'] - int(commodity[res_name]) <= 0:
			print("你的余额不足")
			return
		else:
			shopping_cart.append(res_name)
			yes = input('是否继续购买: Y & N:')
			if yes == 'N':
				for i in shopping_cart:
					data['balance'] = data['balance'] - int(commodity[i])
					money.append(int(commodity[i]))
				logger.info("%s购买了：%s,本次消费共花费：%s,你的账户余额是：%s" % (data['username'], ','.join(shopping_cart),sum(money), data['balance']),data)
				f = open('%s/account/%s.json' % (BASE_DIR, data['username']), 'w')
				json.dump(data, f)

				break

			elif yes == 'Y':
				continue




