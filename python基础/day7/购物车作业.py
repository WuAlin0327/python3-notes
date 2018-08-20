goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
]
shopping_cart = {}
lump = []
sum = 0

shopping = True
user = input("请输入用户名：")
password = input("请输入密码：")

wage = int(input("请输入本月工资："))

print("-----商品列表-----")
for index,i in enumerate(goods):
	print("%s, %s	%s"%(index,i['name'], i['price']))

while shopping: #主循环
	number = input("请输入需要购买的的商品编号：")
	if number.isdigit():
		shopping_cart[goods[int(number)]['name']] = goods[int(number)]['price']#将商品名字与商品价格添加到字典中
		unit = int(goods[int(number)]['price'])
		if unit>wage:
			print("余额不足无法添加到购物车")
		elif unit<wage:
			lump.append(unit)
			for x in lump:
				sum = sum+x #计算购买物品总额       "\033[43;31mxxxx\033[0m"
			banblace = wage - sum  # 计算余额
			price = int(goods[int(number)]['price'])

			if banblace<=0:
				print("你的钱不够不能买这个，已结算！")
				print('\033[43;31m你本次一共消费：%s，余额是： %s\033[0m'%(sum,banblace))
				print("-----购物车中的商品---")
				for k,v in shopping_cart:
					print(k,v)
				shopping = False
			if banblace>price:
				print("该商品已加入购物车，请问还需要购买什么")

	if number == 'q':
		print('\033[43;31m你本次一共消费：%s，余额是： \033[0m'%(sum))
		print("-----购物车中的商品---")
		for commodity in shopping_cart:
			print('		'+commodity)
	