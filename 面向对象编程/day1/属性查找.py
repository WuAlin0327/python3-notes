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
stu1 = LuffyStudent('wualin','man',29)
stu2 = LuffyStudent('张宝宝','man',19)

# 类的数据属性
print(stu1.school)


# 类的函数属性，类中函数属性是给对象使用的，谁调用就绑定给它使用，自动将对象传入第一个参数


stu1.learn()#learn(stu1)

#对象在访问一个属性的时候会先在对象里面的名称空间找，如果对象里面没有则去类里面找。不会到全局变量里面找