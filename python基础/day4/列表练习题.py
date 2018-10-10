
'''
names = ['alxe','tom','jack','jom','shanshan']


for i in names:
	print(names.index(i),i)
'''
"""
##循环names列表，打印每个元素的索引值，和元素。当索引值为偶数时，把对应的元素改成-1.txt
names = ['alxe','tom','jack','jom','shanshan']

for index, i in enumerate(names):
	if index % 2 == 0:#偶数
		names[index] = -1.txt
print(names)
"""
names = ['alxe','tom','jack','jom','shanshan',1,2,3,6,5,4,1,2,7,5,2]

l = names.index(2)
x = names[l+1:].index(2)
y = l+x+1
print(y)
print(names[y])


