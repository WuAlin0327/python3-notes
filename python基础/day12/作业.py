
#使用 while 循环实现输出 2-3+4-5+6...+100的和
# i = 2
# sum = 0
# while i<=100:
# 	if i%2==0:
# 		sum+=i
# 	else:
# 		sum-=i
# 	i+=1
# print(sum)
# i = 0
# while i<=12:
# 	if i==6 or i==10:
# 		pass
# 	else:
# 		print(i)
# 	i+=1

# count = 100
# sum = 0
# while sum <= 50:
# 	if sum <= 50:
# 		print(sum)
# 	sum += 1
# 	while count > 49:
# 		if count>=50:
# 			print(count)
#
#
# 		count-=1

# count = 0
# while count<=100:
# 	if count%2==1:
# 		print(count)
# 	count+=1

# count = 0
# while count <=100:
# 	if count%2==0:
# 		print(count)
# 	count+=1

##用户登陆认证
# user = {'jack':123,'tom':456,'jom':789}
# sum = 0
# l = []
# file = open('user.txt','r')
# f = file.readlines()
# for i in f:
# 	i = i.strip()
# 	l.append(i)
#
# file.close()
# print(l)
# run = True
# while run:
# 	username = input("user:")
# 	password = input("password:")
# 	if username in l:
# 		print("该用户已被锁定")
# 		break
#
# 	elif username in user.keys() and int(password) == user.get(username):
# 		print("登陆成功")
# 		run = False
# 	elif int(password) != user.get(username) or username not in user:
# 		print("登陆失败")
#
# 		if sum == 2:
# 			file = open('user.txt', 'a')
# 			file.write(username + '\n')
# 			file.close()
# 			exit()
#
#
# 	sum+=1
#
# year = int(input("请输入年份："))
# if year %4==0 and year%100!=0:
# 	print("该年份是闰年")
# elif year%400==0:
# 	print("该年份是闰年")
# else:
# 	print("该年份不是闰年")

i = 2
sum = 0
while i<=100:
	if i %2 ==0:
		sum+=i
	else:
		sum-=i
	i+=1
print(sum)
