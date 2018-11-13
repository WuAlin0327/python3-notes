# from multiprocessing import Queue
# #
# # q = Queue(4)#指定队列大小，如果不指定大小则大小为无穷尽
# #
# # q.put('hello')
# # q.put({'a':1})
# # q.put([3,3,3])
# # print(q.full())
# # q.get()


import time
from multiprocessing import Queue,Process

def func(q):

	for i in range(1000):
		dic = {}
		dic['%s'%i] = i
		q.put(dic)
		time.sleep(1)

def func2(q):
	count = 0
	while True:
		count+=1

		print('第%s个数据'%(count),q.get())
		time.sleep(2)

if __name__ == '__main__':
	q = Queue(10)
	p1 = Process(target=func,args=(q,))
	p1.start()
	p1 = Process(target=func2,args=(q,))
	p1.start()