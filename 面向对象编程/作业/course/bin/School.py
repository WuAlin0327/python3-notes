class People:
	def __init__(self,name):
		self.name = name

class Student(People):
	pass

class Teacher(People):
	def __init__(self,name,age):
		super(People,self).__init__(name)
		self.age = age


class School:
	def __init__(self,name,address,city):
		self.name = name
		self.address = address
		self.city = city

class Course:
	def __init__(self,name,price,outline):
		self.name = name
		self.prict = price
		self.outline = outline

