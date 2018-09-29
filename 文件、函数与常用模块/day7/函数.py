# def func(name,age,*args,**kwargs):
# 	print(name,age,args,kwargs['abc'])
# func('wualin','22',222,551,113,nex=21,abc='aabbc')
#
#
# def func1(func):
# 	def inner(num):
# 		print('装饰器，第一个print')
# 		func(num)
# 		print('装饰器，第二个print')
# 		return True
# 	return inner
# @func1
# def print_num(num):
# 	for i in list(range(num)):
# 		print(i)
#
# print(print_num(5))
# def func(num):
# 	if num == 1:
# 		return 1
# 	return num * func(num-1)
# print(func(4))
# 递归：二分查找法
lis = [1,2,3,45,6,6,7,8,9,456,5,242,42,6,363,1]
# def func(data,num):
# 	if len(data) > 1:
# 		meso = int(len(data)/2)
#
# 		if num in data[0:meso]:
# 			print(data[0:meso])
# 			func(data[0:meso],num)
# 		else:
# 			print(data[meso:])
# 			func(data[meso:],num)
# 	else:
# 		print('找到了',data[0])
# func(lis,37)
# 生成式
# num = (i for i in lis)
# print(num)
# for i in num:
# 	print(i)

def func(num):

	while True:
		if num > 0:
			num = num-1
			print(num-1)
			yield num
		else:
			print(num)
			break
func = func(5)
func.__next__()
func.__next__()
func.__next__()
func.__next__()
