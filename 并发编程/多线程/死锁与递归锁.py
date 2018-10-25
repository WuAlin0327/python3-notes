# from threading import Thread,Lock
# mutexA = Lock()
# mutexB = Lock()
#
# mutexA.acquire()
# mutexB.acquire()

# 递归锁
from threading import Thread,Lock
import time
mutexA = Lock()
mutexB = Lock()

class MyThread(Thread):
	def run(self):
		self.f1()
		self.f2()

	def f1(self):
		mutexA.acquire()
		print('%s 拿到了A锁'%self.name)
		mutexB.acquire()
		print('%s 拿到了B锁'%self.name)
		mutexB.release()
		mutexA.release()

	def f2(self):
		mutexB.acquire()
		print('%s 拿到了B锁' % self.name)
		time.sleep(0.1)
		mutexA.acquire()
		print('%s 拿到了A锁' % self.name)
		mutexA.release()
		mutexB.release()

for i in range(10):
	t = MyThread()
	t.start()
