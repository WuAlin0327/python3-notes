# import time
# import random
# from threading import Thread
#
# def run(name):
# 	print('%s is running'%name)
# 	time.sleep(random.randrange(1,5))
# 	print('%s is end'%name)
#
# if __name__ == '__main__':
# 	t1 = Thread(target=run,args=('喵',))
# 	t1.start()
# 	print('主线程')
#
#
import time
from threading import Thread
class MyThread(Thread):
	def __init__(self,name):
		super().__init__()
		self.name = name

	def run(self):
		print('%s is running'%self.name)
		time.sleep(2)
		print('%s is end'%self.name)

if __name__ == '__main__':
	t1 = MyThread('喵')
	t1.start()
	print('主线程')
