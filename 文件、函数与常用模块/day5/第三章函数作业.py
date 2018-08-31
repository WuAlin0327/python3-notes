# 1. 编码问题
'''
1。请说明python2 与 python3中的默认编码是什么
答：python2默认编码是ascll, python3中默认编码是utf-8

2。为什么会出现中文乱码？你能列举出出现乱码的情况有哪几种？
答：1.写入是文件编码与打开的文件编码不一致
	2.文件编码转换错误，比如gbk编码不能直接转utf-8，需要通过uniconde转换

3。如何进行编码转换
答：先使用decode解码为unicode，然后通过encode编码为需要转换的编码

4. #-*-coding:utf-8-*-的作用是什么
答：声明该文件以utf-8编码执行

5。解释py2 bytes vs py3 bytes的区别
答:python2 bytes表示一切二进制流，python3 bytes表示二进制格式，如图片，视频

'''
# 2. 文件处理
'''
1。 r和rb的区别是什么
答：r是以只读形式打开，rb是以二进制只读形式打开

2。 解释一下一下三个参数的分别作用
open(f_name,'r',encoding="utf-8")
答：f_name:打开的文件名
'r'：以只读形式打开该文件
encoding = 'utf-8'：指定文件打开的编码格式

'''
# 3. 函数基础
#1.写函数，计算传入数字参数的和。（动态传参）
# def num(x,y):
# 	a = x+y
# 	print(a)
# num(4,5)
#2.写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件de批量修改操作
# def modify_file(file_name,old,new):
# 	f = open(file_name,'r+')
# 	file= f.read()
# 	file = file.replace(old,new)
# 	f.seek(0)
# 	f.write(file)
# 	f.close()
#
# modify_file('text.txt','123','321')
#3.写函数，检查用户传入的对象（字符串，列表，元组）的每一个元素是否含有空内容
# def cheak(self):
# 	for i in self:
# 		if i==" ":
# 			print("该对象有空内容")
#
#
# l = [1,2,3,4,' ',5]
# cheak(l)
#4.写函数，检查传入字典的每一个value的长度，如果大于2，那么进保留前两个长度的内容，并将新内容返回给调用者
# def cheak(dic):
# 	ret = {}
# 	for key,value in dic.items():
# 		if len(value) > 2:
# 			ret[key] = value[0:2]
# 		else:
# 			ret[key] = value
# 	print(ret)
# 	return ret
#
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# cheak(dic)
#5.解释闭包的概念

#函数进阶：
#1.写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# def func():
# 	taem_list = []
# 	lis = []
# 	for i in range(2,11):
# 		taem_list.append(i)
# 	taem_list.extend(['J','Q','K','A'])
#
# 	for i in taem_list:
# 		for t in ('黑桃', '红心', '梅花', '方块'):
# 			cou = (t,i)
# 			lis.append(cou)
# 	return lis
#
# l = func()
# print(l)
#2.写函数，传入n个数，返回字典{'max':最大值，'min'：最小值}
# def func(num):
# 	dic = {}
# 	dic['max'] = max(num)
# 	dic['min'] = min(num)
# 	return dic
# l = (1,2,3,4,5,6,6,4,3,3,54,6,5,4,)
# s = func(l)
# print(s)

#3.写函数，专门计算图形
#* 其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积
#* 调用函数area（'圆形'，半径）返回圆的面积
#* 调用函数area（'正方形'，周长）返回正方形的面积
#* 调用函数area（'长方形'，长，宽）返回长方形的面积

def area(x,y,shape):
	def round():
		pass

