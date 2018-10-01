class Foo:
	def __init__(self,name):
		self.name = name

	def tell(self):# 绑定到对象的函数
		print('name：%s'%self.name)

	@classmethod
	def func(cls): #cls=Foo	绑定到类的方法
		print(cls)

	@staticmethod
	def func1(x,y):#类中的普通函数
		print(x+y)

f = Foo('wualin')
Foo.func1(1,2)
f.func1(1,3)