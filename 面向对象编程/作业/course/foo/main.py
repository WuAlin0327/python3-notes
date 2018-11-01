import os,sys
import pickle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from bin import admin
from bin import file_pickle
while True:
	print('-----Welcome-----')
	username = input('Username:')
	password = input('Password:')

	if username and password == 'admin':
		while True:
			a = admin.Admin()
			print('''
	-----管理员模式-----
	1.txt. 添加学员
	2. 添加讲师
	3. 创建课程
	4. 创建班级
	5. 给讲师分配课程
	6. 给讲师分配班级
	7. 创建学校
			''')
			num = input('>>>').strip()
			if num == '1.txt':
				a.add_student()
			if num == '2':
				a.add_teacher()
			if num == '3':
				a.add_course()
			if num == '4':
				a.add_team()
			if num == '7':
				a.add_school()

	elif username +'.user_pickle' not in os.listdir('%s/user_pickle/'%BASE_DIR):
		print('该用户不存在，请联系管理员')

	else:
		data = file_pickle.read_file(username)
		if data.number == 1:#判断读取pickle文件中字典的键number是否等于1，如果等于1就是学生登陆，如果是2就是老师登陆
			while True:
				print('''
	-----学生模式----
	1.txt. 购买课程
	2. 查看信息	
	3. 充值		
				''')
				pick = input('请选择：').strip()
				if pick == '1.txt':
					course_list = file_pickle.read_file('course_list')
					for index,i in enumerate(course_list):
						print(index,':',i)
					course_name = int(input('请选择课程序号:').strip())
					course = file_pickle.read_file(course_list[course_name]) #将选择课程序列号传入读取出来的课程列表中，读出对应序列号的元素打开文件对象赋值给course
					for i in course.__dict__:
						print(i,':',course.__dict__[i])
					if int(data.money) < int(course.price):
						print('余额不足，请充值')
					else:
						print('购买成功')
						data.course = course
						file_pickle.write_file(data,data.username)
				elif pick == '2':
					for i in data.__dict__:
						print(i,':',data.__dict__[i])
		elif data.number == 2:
			print('''
-----讲师模式-----
1.txt. 查看课程信息
2. 查看班级
3. 查看学员			
			''')
