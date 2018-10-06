import pickle
import os,sys

USERINFO = 'userinfo'
STUDENTS = 'students_info'
TEACHER = 'teachers_info'
TEAM = 'team_info'
COURSE = 'course_info'

class Team:
	def __init__(self,name,teacher,course):
		self.name = name
		self.teacher = teacher
		self.student = []
		self.course = course
	@staticmethod
	def print_team():
		with open(TEAM,'rb') as f:
			count = 1
			while True:
				try:
					obj = pickle.load(f)
					print(count,obj.name)
					count+=1
				except EOFError:
					break

class Course:
	school = 'LuffyCity'
	def __init__(self,name,price,cycle,teacher,city):
		self.name = name
		self.price = price
		self.cycle = cycle
		self.teacher = teacher
		self.city = city


class People:
	def show_pick_course(self):
		with open('course_info','rb') as f:
			count = 1
			while True:
				try:
					obj = pickle.load(f)
					print(count,obj.name,obj.price,obj.cycle,obj.teacher)
					count+=1
				except EOFError:
					break

class Teacher:
	func_list = [
		('管理班级','manage_team'),
		('查看班级学员','show_student'),
		('修改学生成绩','modify_grade'),
		('退出','exit')
	]
	def __init__(self,name,course,team):
		self.name = name
		self.course = course
		self.team = team

	def show_pick_course(self):
		print(self.course)


	def manage_team(self):
		print('管理班级')
	def show_student(self):
		print(self.team)
	def modify_grade(self):
		print('修改学生成绩')
	@staticmethod
	def init(name):
		with open(TEACHER, 'rb') as f:
			while True:
				try:
					obj = pickle.load(f)
					if name == obj.name:
						return obj
				except EOFError:
					print('')
					break
	def exit(self):
		exit()

class Student(People):
	func_list = [
		('查看可选课程','show_pick_course'),
		('选择课程','pick_course'),
		('选择班级','pick_team'),
		('查看所有信息','show_info'),
		('退出','exit')

	]
	def __init__(self,name):
		self.name = name
		self.course = []


	def pick_course(self):
		super().show_pick_course()
		cour = input('请输入序号：')
		with open('course_info','rb') as f:
			count = 1
			while True:
				try:
					obj = pickle.load(f)
					if count == int(cour):
						self.course.append(obj)
						print('添加%s课程成功'%(obj.name))
						f1 = open(STUDENTS,'rb')
						f2 = open('students_info_new','wb')
						while True:
							try:
								data1 = pickle.load(f1)
								if data1.name == self.name:
									pickle.dump(self,f2)
								else:
									pickle.dump(data1,f2)
							except EOFError:
								break
						os.renames('students_info_new',STUDENTS)

					count += 1
				except EOFError:
					break



	def show_info(self):
		lis = []
		for i in self.course:
			lis.append(i.name)
		print('姓名：%s 已选课程：%s'%(self.name,'|'.join(lis)))
	def pick_team(self):
		Team.print_team()
		cour = input('请输入序号：')
		with open(TEAM, 'rb') as f:
			count = 1
			while True:
				try:
					obj = pickle.load(f)
					if count == int(cour):
						obj.student.append(self)
						print('选择班级成功:%s' % (obj.name))
						f1 = open(TEAM, 'rb')
						f2 = open('team_new', 'wb')
						while True:
							try:
								data1 = pickle.load(f1)
								if data1.name == obj.name:
									pickle.dump(obj, f2)
								else:
									pickle.dump(data1, f2)
							except EOFError:
								break
						os.renames('team_new', STUDENTS)

					count += 1
				except EOFError:
					break


	@staticmethod
	def init(name):
		with open(STUDENTS, 'rb') as f:
			while True:
				try:
					obj = pickle.load(f)
					if name == obj.name:
						return obj
				except EOFError:
					print('没有这个学生')
					break
	def exit(self):
		exit()


class Admin(People):
	func_list = [
		('创建学生','cerate_student'),
		('创建讲师','cerate_teacher'),
		('创建课程','cerate_course'),
		('查看所有课程','show_pick_course'),
		('查看所有学生','show_all_student'),
		('查看所有学生选课情况','show_all_student_course'),
		('创建班级','cerate_team'),
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
		student_obj = Student(username)
		with open(USERINFO,'a',encoding='utf-8') as f:
			f.write('%s|%s|Student\n'%(username,password))
		with open('students_info','ab') as f:
			pickle.dump(student_obj,f)
		print('%s学生创建完成'%(student_obj.name))

	def cerate_teacher(self):
		name = input('Teacher Name:')
		pwd = input('Teacher Pwd:')
		course = input('Course:')
		team = input('Team name:')

		teacher_obj = Teacher(name,course,team)
		with open(TEACHER,'ab') as f1:
			pickle.dump(teacher_obj,f1)
		with open(USERINFO,'a',encoding='utf-8') as f2:
			f2.write('%s|%s|Teacher\n'%(name,pwd))

			print('%s老师创建完成'%teacher_obj.name)



	def cerate_course(self):
		course_name = input('Course_Name:')
		course_price = input('Course_Price:')
		course_cycle = input('Course_Cycle:')
		course_teacher = input('Course_Teacher:')
		course_obj = Course(course_name,course_price,course_cycle,course_teacher)
		with open('course_info','ab') as f:
			pickle.dump(course_obj,f)
		print('%s课程创建成功'%course_obj.name)


	def show_all_student(self):
		with open(STUDENTS,'rb') as f:
			while True:
				try:
					stu_obj = pickle.load(f)
					print(stu_obj.name)
				except:
					break

	def show_all_student_course(self):

		with open(STUDENTS, 'rb') as f:
			while True:
				try:
					lis = []
					obj = pickle.load(f)
					for i in obj.course:
						lis.append(i.name)
					print('%s已选：%s'%(obj.name,'|'.join(lis)))
				except EOFError:
					break
	def cerate_team(self):
		team_name = input('Team Name:')
		team_teacher = input('Team Teacher:')
		course_name = input('Course:')
		with open(TEACHER,'rb') as f1:
			while True:
				try:
					tea_obj = pickle.load(f1)
					if tea_obj == team_teacher:
						tea_obj = Team(team_name,tea_obj,course_name)
						with open(TEAM,'ab') as f:
							pickle.dump(tea_obj,f)
						print('创建班级成功')
				except EOFError:
					break



	def exit(self):
		exit()

	@classmethod
	def init(cls,name):
		return cls(name)

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
				return {'status':False,'name':user}


log = login()


if log['status']:
	if hasattr(sys.modules[__name__],log['cls']): # log['cls']中是登陆成功返回的字符串判断是学生还是管理员
		cls = getattr(sys.modules[__name__],log['cls'])#拿到log['cls']类
							#实例化一个obj对象（传入是学生就实例化一个学生类，传入是管理员就判断是一个管理员类）
		obj = cls.init(log['name'])
		while True:
			for index,i in enumerate(obj.func_list,1):
				print(index,i[0])
			func_num = obj.func_list[int(input('>>>'))-1][1]
			if hasattr(cls,func_num):
				getattr(cls,func_num)(obj)
else:
	print('账号或者密码错误')