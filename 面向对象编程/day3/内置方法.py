# item
# class Foo():
# 	def __init__(self,name):
# 		self.name = name
#
# 	def __getitem__(self, item):#查看
#
# 		return self.__dict__.get(item)
#
# 	def __setitem__(self, key, value):#增加
# 		self.__dict__[key] = value
#
# 	def __delitem__(self, key):#删除
# 		del self.__dict__[key]
#
# obj = Foo('wualin')
# #操作字典的方式去操作obj对象
# #查看
# print(obj['name']) #obj.name
#
# #增加
# obj['age'] = 20 #obj.age = 20
# print(obj['age'])
#
# #删除
# del obj['name'] #del obj.name

class Open():
	def __init__(self,filename):
		print('Open...')

	def __del__(self):
		print('del...')
f = Open('a.txt')
print('---main---')