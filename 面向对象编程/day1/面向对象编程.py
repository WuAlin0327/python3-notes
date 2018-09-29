class LuffyStudent:
	school = 'luffycity' #数据属性

	def learn(self):# 函数属性
		print('is learing')

	def eat(self):
		print('is eating')

# # 查看类的名称空间
# print(LuffyStudent.__dict__)
# print(LuffyStudent.__dict__['school'])
# print(LuffyStudent.__dict__['learn'])

# 查看类的属性
#print(LuffyStudent.school) #LuffyStudent.__dict__['school']

# 增加类的属性
LuffyStudent.county = 'China'

# 删除
del LuffyStudent.county

# 改
LuffyStudent.school = 'Luffycity'