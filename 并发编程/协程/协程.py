import gevent
import time
from gevent import monkey
monkey.patch_all()#给IO打补丁，碰到IO就切换任务

def eat(name):
    print('%s eat 1'%name)
    gevent.sleep(3)
    print('%s eat 2'%name)

def play(name):
    print('%s play 1'%name)
    gevent.sleep(4)
    print('%s play 2'%name)

g1 = gevent.spawn(eat,'miao')
g2 = gevent.spawn(play,'alex')

#遇到io切换任务
g1.join()#异步提交任务，保证所有进程执行完才结束
g2.join()
