class Hero:
	def __init__(self,name,life,attack):
		self.name = name
		self.life = life
		self.attack = attack
	def attack_1(self,enemy):
		print('%s攻击了%s'%(self.name,enemy.name))

class Griren(Hero):
	pass

class Riven(Hero):
	pass

g1 = Griren('盖伦',80,50)
r1 = Riven('锐雯',50,50)

g1.attack_1(r1)