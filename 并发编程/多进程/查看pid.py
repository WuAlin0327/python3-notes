from multiprocessing import Process
import time
import os


def task(name):
	print('%s is running,parent id is <%s>'%(os.getpid(),os.getppid()))
	time.sleep(5)
	print('%s is done'%os.getpid())

if __name__ =='__main__':
	p = Process(target=task,args=('子进程1',))
	p.start() #仅仅只是给操作系统发送了一个信号
	print('主',os.getpid())
