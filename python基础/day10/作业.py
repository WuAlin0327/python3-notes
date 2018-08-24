#请使用代码实现：利用下划线将列表的每一个元素拼接成字符串
# li = ['alex','eric','rain']
# li = '_'.join(li)
# print(li)
#2.查找列表汇总元素，移除每个元素的空格，并查找已a或者A开头 并且已c结尾的所有元素。
#li = ['alec','aric','Alex','Tony','rain']


#3.写代码，有如下列表，按照要求实现每一个功能
#li = ['alex','eric','rain']

#* 计算列表的长度并输出
# li = len(li)
# print(li)

#* 列表中追加元素seven，并输出添加后的列表
#li.append('seven')
#print(li)

#* 请在列表的第一个位置插入元素'tony'，并输出添加后的列表
#li.insert(1,'tony')

#* 请修改列表第二个位置的元素为'kelly'，并输出修改后的列表
#li[2] = 'kelly'
#print(li)

#* 请删除列表中的元素'eric'，并输出修改后的列表
#li.remove('eric')
# print(li)

#* 删除列表中的第二个元素，并输出删除的元素的值余删除元素后的列表
# del li[2]
# print(li)

#* 删除列表中的第三个元素，并输出删除元素后的列表
#del li[3]

#* 请删除列表中的第2至4个元素，并输出删除元素后的列表
# del li[2:4]
# print(li)

#* 请将列表所有的元素反转，并输出反转后的列表
# l2 = li[::-1]
# print(l2)

#* 通过for，len，range输出列表的索引
# for l in range(len(li)):
# 	print(l)

#* 使用enumrate输出列表元素和序号
#
# for index,l in enumerate(li):
# 	print(index,l)
#


#4.写代码，如又下列表，请按照功能要求实现每一个功能
# li = ['hello','seven',['mon',['he','kelly'],'all'],123,456]
# 请根据索引输出kelly
# l1 = li[2][1][1]
# print(l1)
# li[2][2] = 'ALL'
# print(li)
#
# #5.写代码，有如下元组。请按照功能要求实现每一个功能
# tu = ('alex','eric','rain')
# #* 计算元组的长度并输出
# print(len(tu))
# #* 获取元组的第二个元素，并输出
# print(tu[2])
# #*  获取元组第1-2个元素，并输出
# print(tu[1:2])
# #* 请使用for，len，rang输出元组的索引
# for i in range(len(tu)):
# 	print(i)
# #* 请使用enumrate输出元组元素和序号
# for index,t in enumerate(tu):
# 	print(t,index+10)
#
# #6.有如下变量，请实现要求的功能
# tu = ('alex',[11,22,{'k1':'v1','k2':['age','name'],'k3':(11,22,33)},44])
# #* 请讲述元组的特性：
# #答：元组是有序不可变列表
# #* 请问变量tu中的第一个元素'alex'是否可以被修改
# # 不可被修改
# #* 请问tu变量中的'k2'对应的值是什么类型？是否可以被修改？如果可以，请在其后面添加元素'seven
# # tu[1][2]['k2'].append('seven')
# # print(tu)			元组中可变元素不可被更改
# #* tu变量中'k3'对应的值是什么类型...
# # tu变量中k3对应的值是元组类型，不可被修改

#7.字典
dic = {'k1':'v1','k2':'v2','k3':[11,22,33]}
# * 请循环输出所有key
	# print(k)
#* 请循环输出所有value
	# print(dic[k])
#* 请循环输出所有key和value
	# print(k,dic[k])
#*
#*请在字典中添加一个健值对，'k4':'v4',输出添加后的字典
# dic['k4'] = 'v4'
# print(dic)
#* 修改字典中'k1'对应的值为'alex',输出修改后的字典
# dic['k1'] = 'alex'
# print(dic)
#* 请在k3对应的值中追加一个元素44，输出修改后的字典
# dic['k3'].append(44)
# print(dic)
#* 请在k3对应的值的第一个位置插入元素18，输出修改后的字典
# dic['k3'].insert(1,18)
# print(dic)

# 转换
#* 将字符串s = 'alex'转换成列表
# s = 'alex'
# s = list(s)
# print(s)
#* 将字符串s = 'alex'转换成元组
# s = 'alex'
# s = tuple(s)
# print(s)
#* 将列表li = 【'Alex'，'seven'】转换成元组
# li = ['alex','seven']
# li = tuple(li)
# print(li)
#* 将元组tu = ['alex','seven']转换成列表
# tu = ['alex','seven']
# tu = list(tu)
# print(tu)
#* 将列表li = ['alex','seven']转换成字典，且字典的key按照10开始往后递增
# li = ['alex','seven']
# dic = {}
# for index,i in enumerate(li):
# 	dic[index+10] = i
# print(dic)

#9.元素分类
#有如下集合[11,22,33,44,55,66,77,88,99,90],将所有大于66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中
# 即：{'k1':大于66的所有值，'k2':小于66的所有值}
# li = [11,22,33,44,55,66,77,88,99,90]
# l1 = []
# l2 = []
# dic = {}
# for i in li:
# 	if i > 66:
# 		l1.append(i)
# 	if i < 66:
# 		l2.append(i)
# dic['k1'] = l1
#
# dic['k2'] = l2
# print(dic)

