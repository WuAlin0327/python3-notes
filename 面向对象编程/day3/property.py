class People:
	def __init__(self,name):
		self.__name = name
	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self,val):
		if not isinstance(val,str):
			print('val is not str')
			return
		self.__name = val
	@name.deleter
	def name(self):
		print('不允许删除')

p = People('wualin')
print(p.name)