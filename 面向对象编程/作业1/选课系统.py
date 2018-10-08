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
					print(count,obj.city,obj.name,obj.price,obj.cycle,obj.teacher)
					count+=1
				except EOFError:
					break
	@staticmethod
	def get_pickle(path):
		with open(path,'rb') as f:
			while True:
				try:
					obj = pickle.load(f)
					yield obj
				except EOFError:
					break
	@staticmethod
	def dump_pickle(path,obj):
		with open(path,'ab') as f1:
			pickle.dump(obj,f1)


class Teacher(People):
	func_list = [
		('管理班级','manage_team'),
		('查看班级学员','show_student'),
		('修改学生成绩','modify_grade'),
		('退出','exit')
	]
	def __init__(self,name,course):
		self.name = name
		self.course = course


	def show_pick_course(self):
		print(self.course)


	def manage_team(self):
		print('管理班级')
	def show_student(self):
		print('查看班级学生')
	def modify_grade(self):
		print('修改学生成绩')
	@staticmethod
	def init(name):
		for teacher in People.get_pickle(TEACHER):
			if name == teacher.name:
				return teacher

	def exit(self):
		exit()

class Student(People):
	func_list = [
		('查看可选课程','show_pick_course'),
		('选择课程','pick_course'),
		('选择班级','pick_team'),
		('查看所有信息','show_info'),
		('充值','money'),
		('退出','exit')

	]
	def __init__(self,name):
		self.name = name
		self.course = []
		self.off = 0


	def pick_course(self):
		super().show_pick_course()
		cour = input('请输入序号：')
		for index,course in enumerate(self.get_pickle(COURSE),1):
			if int(cour) == index:
				if self.off >= int(course.price):
					self.course.append(course)
					self.off -= int(course.price)
					print('选择课程成功')
				else:
					print('余额不足，请充值')



	def show_info(self):
		lis = []
		for i in self.course:
			lis.append(i.name)
		print('姓名：%s 已选课程：%s 账户余额：%s'%(self.name,'|'.join(lis),self.off))
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

					count += 1
				except EOFError:
					print('没有找到该班级')


	@staticmethod
	def init(name):

		for stu in People.get_pickle(STUDENTS):
			if stu.name == name:
				return stu
		else:
			print('没有这个学生')

	def exit(self):#退出时将数据保存到文件中
		f1 = open(STUDENTS, 'rb')
		f2 = open('students_info_new', 'wb')
		while True:
			try:
				data1 = pickle.load(f1)
				if data1.name == self.name:
					pickle.dump(self, f2)
				else:
					pickle.dump(data1, f2)
			except EOFError:
				break
		os.renames('students_info_new', STUDENTS)
		exit()
	def money(self):
		num = int(input('请输入充值金额：').strip())
		self.off+=num
		print('充值成功，余额：%s'%self.off)


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
		self.dump_pickle(STUDENTS,student_obj)
		print('%s学生创建完成'%(student_obj.name))

	def cerate_teacher(self):
		name = input('Teacher Name:')
		pwd = input('Teacher Pwd:')
		course = input('Course:')

		teacher_obj = Teacher(name,course)
		self.dump_pickle(TEACHER,teacher_obj)
		with open(USERINFO,'a',encoding='utf-8') as f2:
			f2.write('%s|%s|Teacher\n'%(name,pwd))
			print('%s老师创建完成'%teacher_obj.name)



	def cerate_course(self):

		course_name = input('Course_Name:')
		course_price = input('Course_Price:')
		course_cycle = input('Course_Cycle:')
		course_teacher = input('Course_Teacher:')
		if course_name == 'python' or course_name == 'liunx':
			course_city ='北京'
			course_obj = Course(course_name,course_price,course_cycle,course_teacher,course_city)
			self.dump_pickle(COURSE,course_obj)
			print('%s课程创建成功'%course_obj.name)
		elif course_name == 'go':
			course_city = '上海'
			course_obj = Course(course_name, course_price, course_cycle, course_teacher, course_city)
			self.dump_pickle(COURSE, course_obj)
			print('%s课程创建成功' % course_obj.name)


	def show_all_student(self):
		for index,stu in enumerate(self.get_pickle(STUDENTS),1):
			print(index,stu.name)

	def show_all_student_course(self):

		for index,stu in enumerate(self.get_pickle(STUDENTS),1):
			course = [i for i in stu.course]
			lis = []
			for l in course:
				lis.append(l.name)
			print(index,stu.name,'|'.join(lis))

	def cerate_team(self):
		team_name = input('Team Name:')
		team_teacher = input('Team Teacher:')
		course_name = input('Course:')

		for teacher in self.get_pickle(TEACHER):
			if team_teacher == teacher.name:
				team_obj = Team(team_name,teacher,course_name)

				self.dump_pickle(TEAM,team_obj)
				print('创建班级成功')
		else:
			print('创建失败')

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