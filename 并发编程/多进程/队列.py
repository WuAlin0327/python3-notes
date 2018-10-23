from multiprocessing import Queue

q = Queue(4)#指定队列大小，如果不指定大小则大小为无穷尽

q.put('hello')
q.put({'a':1})
q.put([3,3,3])
print(q.full())
q.get()