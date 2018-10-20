# class Student:
# 	count = 0
# 	def __init__(self,name):
# 		self.name = name
# 		Student.count+=1
#
# s = Student('111')
# s2 = Student('1222')
# print(Student.count)
'''
编写游戏角色交互 Garen，所属阵营Demacia，具有昵称，生命值200，攻击力100，具备攻击敌人技能 Riven，所属阵营Noxus，具有昵称，生命值100，攻击力200，具备攻击敌人技能 交互：Garen对象攻击了Riven对象
'''


class Hero:
	def __init__(self,name,life,attack):
		self.name = name
		self.life = life
		self.attack = attack

	def cut(self,enemy):
		enemy.life -= self.attack
		print('%s给了%s一刀'%(self.name,enemy.name))

class Garen(Hero):
	camp = 'Demacia'


class Riven(Hero):
	camp = 'Noxus'

g = Garen('大保健',200,100)
r = Riven('锐萌萌',100,200)
g.cut(r)
