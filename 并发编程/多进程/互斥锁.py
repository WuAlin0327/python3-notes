#牺牲效率实现子进程串行
from multiprocessing import Process,Lock
import time

def tack(name,lock):
	lock.acquire()#加锁
	print('%s,1'%name)
	time.sleep(1)
	print('%s,2'%name)
	time.sleep(1)
	print('%s,3'%name)
	lock.release()#释放锁
if __name__ == '__main__':
	lock = Lock()#实例化锁对象
	for i in range(3):
		p = Process(target=tack,args=('进程%s'%i,lock))#把锁传到子进程中
		p.start()
