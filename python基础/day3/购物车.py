products = [['Iphone',6888],['Macpro',14800], ['小米6',2499],['Coffee',31], ['Book',80],['Nike Shoes',799]]

shopping_cart = []

run = True		#标志位
print("----商品列表----")
for index,p in enumerate(products):
	print("%s. %s	%s"%(index,p[0],p[1]))#打印商品列表

while run:
	shopping = input("请问需要购买什么：")
	if shopping.isdigit():	#判断输入是否是数字
		shopping = int(shopping)
		if shopping >= 0 and shopping < len(products):
			shopping_cart.append(products[shopping])	#往购物车中添加输入数字索引的商品
			#print(shopping_cart)
		else:
			print("商品不存在")

	if shopping == 'q':	#判断输入是否是字母q
		if len(shopping_cart) > 0:
			run = False
			print("-----已选购商品-----")
			for index, p in enumerate(shopping_cart):
				print("%s. %s	%s" %(index,p[0],p[1]))# 打印已选购列表

		run = False


