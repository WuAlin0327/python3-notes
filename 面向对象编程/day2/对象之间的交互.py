class Girlun:
	faction = 'Demasia'
	def __init__(self,name,life,attack):
		self.name = name
		self.life = life
		self.attack = attack
	def attack_1(self,enemy):
		enemy.life = enemy.life-self.attack
		print('%s攻击了%s'%(self.name,enemy.name))


class Riwen:
	faction = 'Demasia'

	def __init__(self, name, life, attack):
		self.name = name
		self.life = life
		self.attack = attack

	def attack_1(self, enemy):
		enemy.life = enemy.life - self.attack
		print('%s攻击了%s' % (self.name, enemy.name))
g1 = Girlun('草丛伦',100,10)
r1 = Riwen('锐萌萌',80,20)
print(r1.life)
g1.attack_1(r1)
print(r1.life)