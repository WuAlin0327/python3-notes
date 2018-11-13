from multiprocessing import Event
e = Event() # 创建了一事件
print(e.is_set())# 查看一个事件的状态，默认是阻塞
e.set() # 将这个事件状态改为True
print(e.is_set())
e.wait()# 根据e.is_set()的值决定是否阻塞,如果是True就是不阻塞，如果是False就是阻塞状态
e.clear() # 将这个事件状态改为False