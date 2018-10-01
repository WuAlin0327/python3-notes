import conf


class People:
	def __int__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex

	def tall_info(self):
		print('Name:%s Age:%s Sex:%s'%(self.name,self.age,self.sex))

	@classmethod
	def from_conf(cls):
		name = conf.name
		age = conf.age
		sex = conf.sex
		obj = cls()
		return obj

p = People.from_conf()
print(p)