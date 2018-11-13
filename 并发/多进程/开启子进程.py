from multiprocessing import Process
import time
import os

class MyProcess(Process):
	def __init__(self,name):
		super().__init__()
		self.name = name

	def run(self):
		print('%s is running '%self.name)
		time.sleep(3)
		print('%s is done '%self.name)
		print('子进程pid',os.getpid())
		print('父进程pid',os.getppid())

if __name__ == '__main__':
	p = MyProcess('妈妈也')
	p.start()
	print('主进程pid',os.getpid())