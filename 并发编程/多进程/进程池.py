'''
线程池:multiprocessing import Pool

'''
from multiprocessing import Pool,Process
import time
import os
def func(i):
	print('%s 进程正在运行'%i,os.getpid())
	time.sleep(2)
	print('%s 进程运行结束'%i,os.getpid())


if __name__ == '__main__':
	pool = Pool(3)
	for i in range(10):
		# pool.apply(func,args=(i,))#同步调用
		pool.apply_async(func,args=(i,)) #异步调用
	pool.close()# 结束进程池接收任务
	pool.join() #感知进程池中的任务执行结束