import pickle,os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from . import people
from . import school
from . import file_pickle
from . import team


class Admin:
	def add_student(self):
		'''
		添加学员
		:return:
		'''

		username = input('Student_Name:').strip()
		password = input('Password:').strip()
		luffy_city = input('Luffy_City:').strip()

		college = file_pickle.read_file(luffy_city)
		student = people.Student(username,password,1,college)
		file_pickle.write_file(student,username) #自定义模块将学生对象写入到.pickle文件

	def add_teacher(self):
		'''
		添加讲师
		:return:
		'''
		username = input('Teacher_Name:')
		password = input('Password:')
		course_name = input('Course:')
		course = file_pickle.read_file(course_name)
		teacher = people.Teacher(username,password,2,course)
		file_pickle.write_file(teacher,username)
	def add_course(self):
		'''
		添加课程
		:return:
		'''
		course_list = []
		course_name = input('Course_Name:')
		price = input('Price:')
		cycle = input('Cycle')
		course = school.Course(course_name,price,cycle)
		file_pickle.write_file(course,course_name)
		course_list.append(course_name)
		file_pickle.write_file(course_list,'course_list',mode='rb+')
	def add_team(self):
		'''
		创建班级
		:return:
		'''
		team_list = []
		team_name = input('Team_Name:')
		course = input('班级绑定的课程：')
		if course + '.user_pickle' in os.listdir('%s/user_pickle/' % BASE_DIR):
			data = file_pickle.read_file(course)
			team_obj = team.Team(team_name,data)
			team_list.append(team_name)
			file_pickle.write_file(team_obj,team_name)
			file_pickle.write_file(team_list,'team_list',mode='rb+')

		else:
			print('课程不存在，请先添加')
	def add_school(self):
		school_name = input('School_City:')
		course_name = input('Course:')
		course = file_pickle.read_file(course_name)
		luffy = school.School(school_name,course)
		file_pickle.write_file(luffy,school_name)



