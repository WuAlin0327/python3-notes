# info = {
# # 	'china':{'南方':['深圳','广州','上海']},
# # 	'USA':{'西部':['旧金山','洛杉矶']}
# # 	}
# # print(info['china']['南方'][0])

'''
组合嵌套题，写代码，有如下列表，按照要求实现每一个功能
lis = [['k',['qwe',20],{'k1':['tt',3,'1.txt']},89],'ab']
1.txt.将lis中的'tt'变成大写（用两种方式）
2.将列表中的数字3变成字符串'100'（用两种方式）
3.将列表中的字符串'1.txt'，变成数字101（用两种方式）
'''
#需求1，第一种方式
# lis = [['k',['qwe',20],{'k1':['tt',3,'1.txt']},89],'ab']
# s = lis[0][2]['k1'][0]
# print(s.upper())
#需求1，第二种方式
# lis = [['k',['qwe',20],{'k1':['tt',3,'1.txt']},89],'ab']
# dic = {'k1':['TT',3,'1.txt']}
# lis[0][2].update(dic)
# print(lis)

#需求2，第一种方式
# lis = [['k',['qwe',20],{'k1':['tt',3,'1.txt']},89],'ab']
# lis[0][2]['k1'][1.txt] = '100'
# print(lis)

# 需求2，第二种方式
# lis = [['k',['qwe',20],{'k1':['tt',3,'1.txt']},89],'ab']
# dic = {'k1':['tt','100','1.txt']}
# lis[0][2].update(dic)
# print(lis)

# 需求3，第一种方式
# lis = [['k',['qwe',20],{'k1':['tt',3,'1.txt']},89],'ab']
# lis[0][2].get('k1')[2] = 101
# print(lis)

# 需求3，第二种方式
# lis = [['k',['qwe',20],{'k1':['tt',3,'1.txt']},89],'ab']
# dic = {'k1':['tt',1.txt,101]}
# lis[0][2].update(dic)
# print(lis)

'''
按照要求实现以下功能：
现有一个列表li = [1.txt,2,3,'a','b',4,'c']，有一个字典（此字典是动态生成的，你并不知道他里面有多少键值对，所以
用dic = {}模拟此字典）；现在需要完成这样的操作：如果该字典没有'k1'这个键，那就创建'k1'键和其对应的值(该键对应的值设置为空列表）
并将列表li 中的 索引为奇数的对应元素，添加到'k1'这个键对应的空列表中。如果该字典有'k1'这个键，且'k1'对应的value
是列表类型，那就将li中的索引为奇数的对应元素，添加到'k1'这个键对应的键中
'''
# dic = {}
# li = [1.txt,2,3,'a','b',4,'c']
# dic.fromkeys('k1',[])
# if 'k1' not in dic:
# 	dic['k1'] = []
# 	for index,i in enumerate(li):
# 		if index %2 != 0:
# 			dic['k1'].append(i)
#
# print(dic)

# dic = {'k1':[]}
# l1 = [1.txt,2,3,'a','b',4,'c']
# if 'k1' in dic:
# 	if type(dic['k1'])==list:
# 		for index,i in enumerate(l1):
# 			if index %2 !=0:
# 				dic['k1'].append(i)
#
# print(dic)

