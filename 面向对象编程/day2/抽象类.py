import abc
class Animal(metaclass=abc.ABCMeta):# 通过抽象类使子类中的方法名统一起来
	@abc.abstractmethod
	def run(self):
		pass

	@abc.abstractmethod
	def eat(self):
		pass

class People(Animal):

	def run(self):
		pass

	def eat(self):
		pass

class Pig(Animal):

	def run(self):
		pass

	def eat(self):
		pass
