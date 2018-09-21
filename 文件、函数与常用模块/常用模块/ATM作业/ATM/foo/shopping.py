import json,os
import configparser


BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def shopping(balance):
	res = []

	config = configparser.ConfigParser()
	config.read('%s/conf/commodity.ini'%(BASE_DIR))
	commodity = config['COMMODITY']
	print("--- 商品列表 ---")
	for i in commodity:

		res.append(i)

	#num = int(input("请选择需要购买物品的编号："))





