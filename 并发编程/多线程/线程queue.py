import queue
# q = queue.Queue(3) #先进先出->队列
# q.put(5)
# q.put('miao')
# q.put('sta')
#
# print(q.get())
# print(q.get())
# print(q.get())
#
# #get 和 put可设置是否阻塞以及阻塞时间
#
# print(q.get(block=True,timeout=3))
#
# q = queue.LifoQueue(3)#后进先出->堆栈
#
# q.put('fisrt')
# q.put(2)
# q.put('miao')
#
# print(q.get())
# print(q.get())
# print(q.get())
# import queue
# q = queue.PriorityQueue(3)#优先级队列
# q.put((10,'one'))
# q.put((40,'two'))
# q.put((20,'three'))
# #数字越小优先级越高
# print(q.get())
# print(q.get())
# print(q.get())