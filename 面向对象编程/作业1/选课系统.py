import pickle
import os,sys

USERINFO = 'userinfo'

class Course:
	def __init__(self,name,price,cycle,teacher):
		self.name = name
		self.price = price
		self.cycle = cycle
		self.teacher = teacher

class Teacher:
	def __init__(self,name):
		self.name = name
		self.course = []

	def show_pick_course(self):
		print('查看所选课程')

	def show_student(self):
		print('查看所有学生')

	def show_team(self):
		print('查看所在班级')

class Student:
	func_list = [
		('查看可选课程','show_pick_course'),
		('选择课程','pick_course'),
		('查看所有信息','show_info')

	]
	def __init__(self,name):
		self.name = name
		self.course = []

	def show_pick_course(self):
		print('查看可选课程')

	def pick_course(self):
		print('选择课程')

	def show_info(self):
		print('查看所有信息')


class Admin:
	func_list = [
		('创建学生','cerate_student'),
		('创建讲师','cerate_teacher'),
		('创建课程','cerate_course'),
		('查看所有课程','show_all_course'),
		('查看所有学生','show_all_student'),
		('查看所有学生选课情况','show_all_student_course'),
		('退出','exit')
	]
	def __init__(self,name):
		self.name = name


	def cerate_student(self):
		'''
		将学生用户名与密码写到userinfo文件中
		将学生对象写入student_info
		:return:
		'''
		username = input('UserName:')
		password = input('Password:')
		with open(USERINFO,'a',encoding='utf-8') as f:
			f.write('%s|%s|Student\n'%(username,password))



	def cerate_teacher(self):
		print('创建讲师')

	def cerate_course(self):
		print('创建课程')

	def show_all_course(self):
		print('查看所有课程')

	def show_all_student(self):
		print('查看所有学生')

	def show_all_student_course(self):
		print('查看所有学生选课情况')

	def exit(self):
		exit()

def login():
	username = input('UserName:')
	password = input('Password:')
	with open(USERINFO,'r',encoding='utf-8') as f:
		while True:
			try:
				user,pwd,perm = f.readline().strip().split('|')
				if username == user and password == pwd:
					print('登陆成功')
					return {'status':True,'name':user,'cls':perm}

			except ValueError:
				return {'status':False}

log = login()
if log['status']:
	if hasattr(sys.modules[__name__],log['cls']): # log['cls']中是登陆成功返回的字符串判断是学生还是管理员
		cls = getattr(sys.modules[__name__],log['cls'])#拿到log['cls']类
		obj = cls(log['name'])#实例化一个obj对象（传入是学生就实例化一个学生类，传入是管理员就判断是一个管理员类）
		while True:
			for index,i in enumerate(obj.func_list,1):
				print(index,i[0])
			func_num = obj.func_list[int(input('>>>'))-1][1]
			if hasattr(cls,func_num):
				getattr(cls,func_num)(cls)
