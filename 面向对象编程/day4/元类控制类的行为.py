class Mymeta(type):
	def __init__(self,class_name,class_bases,class_dic):

		'''
		控制类的行为
		'''
		if '__doc__' not in class_dic or not class_dic['__doc__'].strip():#元类必须要有注释，否则抛出异常
			raise TypeError('注释不能为空')
	def __call__(self, *args, **kwargs):
		'''
		元类控制实例化对象的行为
		实例化对象的步骤：
		1. 创造一个obj
		2. 初始化一个obj
		3. 返回一个obj
		:param args:
		:param kwargs:
		:return:
		'''
		obj = object.__new__(self)
		self.__init__(obj,*args,**kwargs)
		return obj

class Chinese(metaclass=Mymeta):
	'''
	xxx
	'''
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def tall_info(self):
		print('Name:%s Age:%s'%(self.name,self.age))

obj = Chinese('wualin',22)
print(obj.__dict__)