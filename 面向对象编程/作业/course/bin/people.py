class People:
	def __init__(self,username,password,number):
		self.username = username
		self.password = password
		self.number = number



class Student(People):
	def __init__(self,username,password,number,school,money=0):
		super().__init__(username,password,number)
		self.school = school
		self.money = money


	def get_teacher(self,teacher): #传入一个老师对象，将老师和学生绑定在一起
		self.teacher = teacher
		self.teacher_name = teacher.username

	def see_info(self):
		for i in self.__dict__:
			print(i,':',self.__dict__[i])
	def pick_team(self,team):
		self.team = team

class Teacher(People):
	student_list = []
	def __init__(self,username,password,number,course):
		super().__init__(username,password,number)
		self.course = course
	def get_student(self,student): #传入一个学生对象，将学生名字添加到老师所在的学生列表中
		self.student_list.append(student.username)