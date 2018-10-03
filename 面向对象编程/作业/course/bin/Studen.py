import configparser,os
import pickle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

conf = configparser.ConfigParser()
conf.read('%s/conf/config.ini'%(BASE_DIR))
conf.sections()
class Studen():
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex


	def __course(self):
		cou = input('请选择课程：').upper()
		self.course_name = conf[cou]['name']
		self.course_price = conf[cou]['price']
		self.course_cycle = conf[cou]['cycle']

		dic = {
			'name':self.name,
			'age':self.age,
			'sex':self.sex,
			'course_name':self.course_name,
			'course_price':self.course_price,
			'course_cycle':self.course_cycle
		}
		return dic
	def save(self):
		f = open('%s/pickle/%s.pickle'%(BASE_DIR,self.name),'wb')
		info = self.__course()
		pickle.dump(info,f)
		for i in info:
			print(i,':',info[i])