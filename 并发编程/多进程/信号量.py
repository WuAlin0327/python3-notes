from multiprocessing import Process
from multiprocessing import Semaphore
import time
import random

def wc(i,sem):
	sem.acquire()
	print('%s 在上厕所'%i)
	time.sleep(random.randint(1,5))
	print('%s 上完厕所了'%i)
	sem.release()

if __name__ == '__main__':
	sem = Semaphore(5)
	for i in range(20):
		p = Process(target=wc,args=(i,sem))
		p.start()
