
# 指名道姓的重用父类的方法：
# class Hero:
# 	def __init__(self,name,life,attack):
# 		self.name = name
# 		self.life = life
# 		self.attack = attack
# 	def attack_1(self,enemy):
# 		enemy.life -=self.attack
#
# class Griren(Hero):
# 	def attack_1(self,enemy):
# 		Hero.attack_1(self,enemy) # 不依赖于继承
# 		print('%s攻击了%s'%(self.name,enemy.name))
# class Riven(Hero):
# 	pass
#
# g1 = Griren('盖伦',80,50)
# r1 = Riven('锐雯',100,50)
# print(r1.life)
# g1.attack_1(r1)
# print(r1.life)

# 方式二：super()
class Hero:
	def __init__(self,name,life,attack):
		self.name = name
		self.life = life
		self.attack = attack
	def attack_1(self,enemy):
		enemy.life -=self.attack

class Griren(Hero):

	def __init__(self,name,life,attack,weapon):
		super().__init__(name,life,attack)# 第一种写法，依赖于继承
	def attack_1(self,enemy):
		super(Griren,self).attack_1(enemy)# 第二种写法，依赖于继承
		print('%s攻击了%s'%(self.name,enemy.name))
class Riven(Hero):
	pass

g1 = Griren('盖伦',80,50,'大保健')
r1 = Riven('锐雯',100,50)
print(r1.life)
g1.attack_1(r1)
print(r1.life)
print(g1.__dict__)