# li = ['手机','电脑','鼠标垫','游艇']
# run = True
# print('-----商品列表-----')
# for index, i in enumerate(li):
# 	print(index, i)
# while run:
#
# 	num = input('请输入需要添加的物品或者需要显示商品的序号')
# 	if num.isdigit():
# 		print(li[int(num)])
# 	if num == 'l':
# 		print(li)
# 	elif num.isalpha():
# 		li.append(num)
# 		print("添加成功")
#

##交集
# l1 = {'tom','jack','jom','tonny'}
# l2 = {'tom','jom'}
# print(l1.intersection(l2))
# print(l1&l2)

# 合集
# l1 = {'tom','jack','jom','tonny'}
# l2 = {'tom','jom','lisa','namei'}
# print(l1.union(l2))
# print(l1|l2)

#差集
# l1 = {'tom','jack','jom','tonny'}
# l2 = {'tom','jom','lisa','namei'}
# print(l1.difference(l2))
# print(l1-l2)

# 对称差集
# l1 = {'tom','jack','jom','tonny'}
# l2 = {'tom','jom','lisa','namei'}
# print(l1.symmetric_difference(l2))
# print(l1^l2)