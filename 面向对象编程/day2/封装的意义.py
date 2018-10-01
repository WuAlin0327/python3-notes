class People:
	def __init__(self,name,age):
		self.__name = name
		self.__age = age

	def tell_info(self):
		print('name:<%s>')