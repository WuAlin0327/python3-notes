from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import os,time,random

def task(name):
	print('name:%s pid:%s run'%(name,os.getpid()))
	time.sleep(random.randint(1,3))


if __name__ == '__main__':
	pool = ProcessPoolExecutor(4)#进程池
	for i in range(10):
		pool.submit(task,'egon%s'%i)#异步调用

	pool.shutdown()#把往进程池提交任务的入口关闭

	print('主')