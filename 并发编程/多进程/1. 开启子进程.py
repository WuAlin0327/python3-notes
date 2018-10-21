# 方式1
# from multiprocessing import Process
# import time
#
# def task(name):
# 	print('%s is running'%name)
# 	time.sleep(5)
# 	print('%s is done'%name)
#
# if __name__ =='__main__':
# 	p = Process(target=task,args=('子进程1',))
# 	p.start() #仅仅只是给操作系统发送了一个信号
# 	print('主')
#方式二：自定义类继承自process
from multiprocessing import Process
import time
class MyProcess(Process):
	def __init__(self,name):
		super().__init__()
		self.name = name

	def run(self): #函数名必须是run
		print('%s is running'%self.name)
		time.sleep(5)
		print('%s is done'%self.name)

if __name__ == '__main__':
	p = MyProcess('子进程1')
	p.start()#本质就是在调用p.run
	print('进')