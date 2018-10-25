from concurrent.futures import ThreadPoolExecutor
import time,random

def eat(name):
	print('%s is eating'%name)
	time.sleep(random.randint(2,5))
	res = random.randint(5,10)*'#'
	return {'name':name,'size':res}

def count(weith):
	weith = weith.result()#
	name = weith['name']
	size = len(weith['size'])
	print('name:%s eat is %s'%(name,size))

if __name__ == '__main__':
	pool = ThreadPoolExecutor(5)
	pool.submit(eat,'miao').add_done_callback(count)#回调机制
	pool.submit(eat,'car').add_done_callback(count)
	pool.submit(eat,'dog').add_done_callback(count)
	pool.submit(eat,'zhang').add_done_callback(count)