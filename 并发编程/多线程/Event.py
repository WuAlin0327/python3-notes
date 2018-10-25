from threading import Thread,Event
import time
event = Event()
def student(name):
	print('学生 %s正在听课'%name)
	event.wait()
	print('学生%s下课了'%name)

def teacher(name):
	print('老师%s 正在上课'%name)
	time.sleep(7)
	print('老师%s 让学生下课了'%name)
	event.set()

if __name__ == '__main__':
	s1 = Thread(target=student,args=('wualin',))
	s2 = Thread(target=student,args=('wxx',))
	s3 = Thread(target=student,args=('zxx',))
	t1 = Thread(target=teacher,args=('egon',))
	s1.start()
	s2.start()
	s3.start()
	t1.start()