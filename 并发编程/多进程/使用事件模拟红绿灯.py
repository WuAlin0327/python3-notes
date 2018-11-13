import time
import random
from multiprocessing import Process,Event

def light(e):
	while True:
		if e.is_set():
			e.clear()
			print('红灯亮了')
		else:
			e.set()
			print('绿灯亮了')
		time.sleep(5)
def cars(i,e):
	if not e.is_set():
		print('%s 在等待'%i)
		e.wait()
	print('%s 通行了'%i)


if __name__ == '__main__':
	e = Event()
	p1 = Process(target=light,args=(e,))
	p1.start()
	for i in range(20):
		p = Process(target=cars,args=(i,e))
		p.start()
		time.sleep(2)