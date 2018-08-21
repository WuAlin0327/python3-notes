dic = {}
lis = []
_user = {}
goods = [
   {'name':'MacBook','price':3999},
   {'name':'Nike','price':500},
   {'name':'GTA5','price':198},
   {'name':'superme','price':50}
]

user = {'jack':123,'tom':456}
username = input('请输入用户名：')
password = input('请输入密码：')
if int(password) == user[username]:
	print('登陆成功')

	wage = input('工资：')
	sum = int(wage)
	run = True
	print('-----商品列表-----')
	for index,l in enumerate(goods):
		print(index,l['name'],l['price'])#输入工资后打印商品列表

	while run:#主循环
	   number = input('请输入编号（输入q退出）：')
	   if number.isdigit():
		  if sum >= goods[int(number)]['price']:
			 dic[goods[int(number)]['name']] = goods[int(number)]['price']
			 if goods[int(number)]['price'] in lis:
				print('请勿重复添加')
			 else:
				lis.append(dic[goods[int(number)]['name']])
				print('已加入购物车')
				sum-=lis[-1]
				print('余额是：',sum)
		  elif sum < goods[int(number)]['price']:
			 print('不够')
	   elif number == 'q':
		  print('-----已购买商品列表-----')

		  for k in dic:
			 print('       ',k)

		  print('余额是：%s'%(sum))
		  break
	else:
		print('登陆失败')
			continue


