# class MySQL:
# 	'''
# 	假如一个类初始化属性都是一样的，可以使用单例模式节省内存空间
# 	'''
# 	__instance = None
# 	def __init__(self):
# 		self.host = '127.0.0.1.txt'
# 		self.port = 3306
#
# 	@classmethod
# 	def singleton(cls): #单例模式函数，生成实例化对象时调用该函数
# 		if not cls.__instance:
# 			obj=cls()
# 			cls.__instance=obj
# 		return cls.__instance
# # 两次实例化对象内存地址是一样的
# obj1 = MySQL.singleton()
# obj2 = MySQL.singleton()
class Mymeta(type):
	def __init__(self,class_name,class_bases,class_dic):
		if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
			raise TypeError('注释不能为空')

		super(Mymeta,self).__init__(class_name,class_bases,class_dic)

		self.__instance = None
	def __call__(self, *args, **kwargs):
		if not self.__instance:
			obj = object.__new__(self)
			self.__init__(obj)
			self.__instance = obj
		return self.__instance

class Mysql(object,metaclass=Mymeta):
	'''
	xxx
	'''
	def __init__(self):
		self.host = '127.0.0.1.txt'
		self.port = 3306

obj1 = Mysql()
obj2 = Mysql()
print(obj1 is obj2)