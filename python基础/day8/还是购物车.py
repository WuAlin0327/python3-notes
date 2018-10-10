import json

goods = [
   {'name':'MacBook','price':3999},
   {'name':'Nike','price':500},
   {'name':'GTA5','price':198},
   {'name':'superme','price':50}
]
article = []
price = []
total = 0
user = {'jack':123,'tom':456}

count = 0
while count <= 2:
	username = input('请输入用户名：')
	password = input('请输入密码：')
	if int(password) == user[username]:#验证用户名与密码是否正确
		print("\033[1.txt;32;40m登陆成功\033[0m")
		wage = input("请输入工资：")
		balance = int(wage)#余额
		print('-----商品列表-----')
		for index,i in enumerate(goods):
			print(index,goods[index]['name'],goods[index]['price'])#打印商品列表
## "\033[43;31mxxxx\033[0m"

		while True:#循环购买物品
			number = input('请输入需要购买物品的编号(退出请按字母，查询消费记录请按空格):')
			if number.isdigit():#判断输入是否是数字
				if balance >= goods[int(number)]['price']:#判断余额是否大于物品价格
					article.append(goods[int(number)]['name'])#将商品名添加到商品列表中
					price.append(goods[int(number)]['price'])#将商品单价添加到价格列表中
					balance = balance-price[-1]#计算余额
					print("\033[43;31m已加入购物车，你的余额是：%s\033[0m"%(balance))
				elif balance < goods[int(number)]['price']:#余额小于商品单价
					print('抱歉，你的余额不足，无法购买')

			elif number == ' ':#查询消费记录
				file = open(username+'.txt', 'r')
				f = file.readlines()
				f = list(f)
				print('%s 你的消费记录如下：'%(f[0]))
				print('购买记录：%s'%(f[-2]))
				print('余额：%s'%(f[-1]))
				pass


			elif number.isalpha():#判断输入是否是字母，是字母则打印购物车信息，跳出循环
				print('-----购物车中的商品-----')
				for i in article:
					print('		',i)
				for x in price:
					total+=x
				print('本次消费：%s，余额是：%s'%(total,balance))
				f = open(username+'.txt','w')
				f.write(username+'\n')
				f.write(json.dumps(article)+'\n')
				f.write(str(balance))
				f.close()
				exit()
	else:
		print('用户名或密码错误,请重新输入！')
		count+=1

