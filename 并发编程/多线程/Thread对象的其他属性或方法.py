from threading import Thread,currentThread,active_count,enumerate

import time

def task():
	print('%s is running'%currentThread().getName())
	time.sleep(2)
	print('%s is done'%currentThread().getName())

if __name__ == '__main__':
	t = Thread(target=task,name='子线程')
	t.start()
	#t.setName('儿子进程1')  设置线程名字
	print(t.isAlive())#判断线程是否存活
	print('主线程',currentThread().getName())
	# t.join()#等当前线程结束才继续执行主线程
	print(active_count())	#活跃的线程数
	print(enumerate())#[<_MainThread(MainThread, started 140735697388416)>, <Thread(子线程, started 123145519529984)>]
