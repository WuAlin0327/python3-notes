#关键字参数
# def sum(a,b,c,d=6):
# 	print(a,b,c,d)
# sum(2,3,5)

#非固定参数
# 方式一
# def sum(a,b,*c):
# 	for i in c:
# 		print(i)
# 	print(a,b,c)
# sum(2,3,3,4,5,6,7,8)
# 方式二
# def sum(a,b,*c):
# 	for i in c:
# 		print(i)
# 	print(a,b,c)
# sum(2,3,*[2,3,4,5,6,7,8,6])

## **
# 方式一：
# def sum(a,*b,**c):
# 	print(a,b,c)
# sum(2,3,4,5,6,d=22,x=444,z=333)

# 方式二：
# def sum(a,*b,**c):
# 	print(a,b,c)
# s = {'str':'x'}
# sum(2,**s)

