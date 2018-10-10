class LuffyStudent:
	school = 'luffycity' #数据属性
	def __init__(self,name,sex,age):# __init__方法用来对象定制对象独有的特征
		self.Name = name
		self.Sex = sex
		self.Age = age

	def learn(self):# 函数属性
		print('is learing')

	def eat(self):
		print('is eating')

# 后产生的对象
stu1 = LuffyStudent('wualin','man',29)#LuffyStudent.__init__(stu1,'wualin','man',20)

# 加上__init__方法后，实例化步骤
'''
1.txt. 先产生一个空对象stu1
2. 触发LuffyStudent.__init__(stu1,'wualin','man',29)
'''
#
# # 查
# print(stu1.Name)
# print(stu1.Sex)
# print(stu1.Age)
# # 改
# stu1.Name='520'
#
# # 删除
# del stu1.Name
#
# # 增
# stu1.class_name = 'python开发'
