import json

goods = [
	{"name": "电脑", "price": 1999},
	{"name": "鼠标", "price": 10},
	{"name": "游艇", "price": 20},
	{"name": "美女", "price": 998},
]
dic = {}
article = []
price = []
total = 0
banlance = 0
user = {'jack':123,'tom':456,'alex':789}
count = 0
run = True



while count <= 2:#登陆验证，账号密码连续三次输入错误结束程序
	username = input('请输入用户名：')
	password = input('请输入密码：')
	if int(password) == user[username]:#判断用户名与密码是否正确
		print("\033[1;32;40m登陆成功\033[0m")
		dic['name'] = username
		dic['commodit'] = ''
		dic['banlance'] = 0
		file = open(username+'.txt','r+')
		f = json.loads(file.readline())
		file.close()
		if f['name'] == username:
			if f['banlance']<=10:
				wage = input("请输入工资：")

				banlance = int(wage)#余额
			else:
				banlance = f['banlance']
		print('-----商品列表-----')
		for index,i in enumerate(goods):
			print(index,goods[index]['name'],goods[index]['price'])#打印商品列表
		print("\033[1;31;40m温馨提示：敲击数字选择对应商品，敲击回车查询消费记录，敲击其他字母退出购买\033[0m")
		while run:
			number = input("请输入商品编号：")
			if number.isdigit():
				if banlance >= goods[int(number)]['price']:#判断余额是否大于物品价格
					article.append(goods[int(number)]['name'])#将商品添加到已购买商品列表
					price.append(goods[int(number)]['price'])#将商品价格添加到已购买商品价格列表
					dic['commodit'] = article
					banlance = banlance-price[-1]#计算余额
					dic['banlance'] = banlance
					print("已购买该物品，你的余额还剩：\033[1;31;40m%s\033[0m"%(banlance))#输出提示
				elif banlance < goods[int(number)]['price']:
					print("你的余额已不足购买该物品")
			elif number == '':#输出回车查询消费记录
				fil = open(username+'.txt','r')
				f = json.loads(fil.readline())
				print('%s 你好！'%(f['name']))
				print('-------上次消费记录-------')
				for i in f['commodit']:
					print('	  ',i)
				print('你的余额是：%s'%f['banlance'])
			elif number.isalpha():#输入字母结束程序，输入已购买商品列表以及余额
				print('-----已购买商品-----')
				for i in article:
					print('		',i)
				for x in price:
					total+=x
				print('你本次消费：%s，你的余额是：%s'%(total,banlance))

				file = open(username+'.txt','w')#将消费记录写入到文件
				file.write(json.dumps(dic))
				file.close()
				exit()

	else:
		print("用户名或者密码错误！请重新登陆")
		count+=1

