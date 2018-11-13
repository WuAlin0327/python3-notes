# from multiprocessing import Process,Queue
# import time
# def producer(q):
# 	for i in range(3):
# 		res = '包子%s'%i
# 		time.sleep(0.5)
# 		q.put(res)
# 		print('生产者生产了%s'%res)
#
# def consumer(q):
# 	while True:
# 		res = q.get()
# 		if res == None:break
# 		time.sleep(0.7)
# 		print('消费者吃了%s'%res)
#
#
# if __name__ == '__main__':
# 	q = Queue()
# 	p1 = Process(target=producer,args=(q,))
# 	c1 = Process(target=consumer,args=(q,))
# 	p1.start()
# 	c1.start()
# 	p1.join()
# 	c1.join()
# 	q.put(None)

from multiprocessing import Process,JoinableQueue
import time
def producer(q):
	for i in range(3):
		res = '包子%s'%i
		time.sleep(0.5)
		q.put(res)
		print('生产者生产了%s'%res)
	q.join() #阻塞，直到一个队列中的所有数据，全部被处理完毕

def consumer(q):
	while True:
		res = q.get()
		time.sleep(0.7)
		print('消费者吃了%s'%res)
		q.task_done() # 处理完一个数据，队列中的计数器-1


if __name__ == '__main__':
	q = JoinableQueue()
	p1 = Process(target=producer,args=(q,))
	c1 = Process(target=consumer,args=(q,))
	p1.start()
	c1.daemon = True #守护进程，主进程中的代码执行完毕后，子进程自动结束
	c1.start()
	p1.join()