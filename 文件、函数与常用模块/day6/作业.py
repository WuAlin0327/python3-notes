# 计算圆，正方形，长方形面积
# def area(*number,shape = ''):
# 	'''
# 	1.编写三个计算形状面积计算公式
# 	2.通过判断shape传入参数是什么形状，number传入边长与半径
#
# 	:param shape:
# 	:param number:
# 	:return:
# 	'''
#
# 	def square():
# 		area1 = int(*number)*int(*number)
# 		return area1
#
# 	def rectangle():
# 		x,y = int(number[0]),int(number[1])
# 		return x * y
#
# 	def round():
# 		pi = 3.14
# 		r = int(*number) * int(*number)
# 		return pi * r
# 	if shape == '':
# 		pass
# 	if shape == 'square':
# 		print(square())
# 	if shape == 'rectangle':
# 		print(rectangle())
# 	if shape == 'round':
# 		print(round())
# area(4,shape='square')
# area(*[2,2],shape='rectangle')

# 计算一个数的阶乘
# def cal(n):
# 	if n == 1:
# 		return 1
# 	sum = n * cal(n-1)
# 	return sum
# print(cal(4))

# 编写装饰器，为多个函数加上认证功能（用户账号密码来自文件），要求登陆成功一次后，后续函数都无需再输入用户名和密码
# logged_in = False
# def login(func):
# 	def inner(*arg):
# 		global logged_in
# 		if logged_in == False:
# 			l = []
# 			f = open('info.txt','r')
# 			file = f.readlines()
# 			for f in file:
# 				l.append(f.strip().split(','))
# 			username = input("username：")
# 			password = input("password：")
# 			for index,i in l:
# 				if username+password == index + i:
# 					print("登陆成功")
# 					logged_in = True
# 					func(*arg)
#
# 		else:
# 			func(*arg)
# 	return inner
# @login
# def music(*arg):
# 	print("---音乐区---",*arg)
#
# @login
# def movie(*arg):
# 	print("---电影区---",*arg)
#
# @login
# def book(*arg):
# 	print("---书本区---",*arg)
# book('言情','喵喵喵')		#book()相当于 book = login(book)再去执行book，
# movie('好莱坞')
# music('古典')

# 生成器和迭代器的区别：
#答：迭代器仅是一容器对象，它实现了迭代器协议，它有两个基本方法，next，__iter__
 #生成器返回列表元素的函数来完成简单和有效的代码，它基于yidle指令

# import datetime
# print(datetime.datetime.now().strftime('%y-%m-%d  %H:%M:%s'))
# count = 0
#
# f = open('datetime.txt','r+')
# while count <= 10:
# 	f.write(datetime.datetime.now().strftime('%y-%m-%d  %H:%M:%s')+'\n')
# 	count+=1
# f.close()
# r = open('datetime.txt','r')
# read = r.read()
# print(read)
import datetime
def logger(filename,channel='file'):
	def number(n):
		while True:
			n = n+1
			yield n
	num = number(0)


	while True:

		a=num.__next__()
		now_time = datetime.datetime.now().strftime('%y-%m-%d  %H:%M:%s ' + '[%s]'%(a))
		ss = yield
		if ss == None:
			ss = ''
		else:
			ss = ss
		if channel == 'file':
			f = open(filename,'r+')
			f.write(now_time)
			f.close()
		if channel == 'terminal':
			print(now_time)
		if channel == 'both':
			f = open(filename,'r+')
			f.writelines(now_time)
			f.close()
			print(now_time,ss)

log_obj = logger(filename='datetime.txt',channel='both')
log_obj.__next__()
log_obj.__next__()
log_obj.__next__()
log_obj.__next__()
log_obj.send('user alex login success')