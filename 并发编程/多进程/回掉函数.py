# from multiprocessing import Pool
# import os
# def func1(i):
# 	print('in func1',os.getpid())
# 	return i*i
#
# def func2(ii):
# 	print('in func2',os.getpid())
# 	print(ii)
#
# if __name__ == '__main__':
# 	'''
# 	1. func1执行结果当作func2的参数，func1进程执行结束后返回结果，通过callback调用func2，将func1的执行返回结果当作参数传递给func2执行
# 	2. func1是一个新的进程
# 	3. func2是在主进程中执行的
# 	'''
# 	p = Pool(5)
# 	p.apply_async(func1,args=(2,),callback=func2)
# 	p.close()
# 	p.join()
import requests
from multiprocessing import Pool
import time
def get_url(url):
	res = requests.get(url)
	if res.status_code == 200:
		return url,res.text
	time.sleep(1)

def call_back(args):
	url,res = args
	print(url,len(res))

if __name__ == '__main__':
	url_list = [
		'https://www.cnblogs.com/wualin/',
		'http://www.baidu.com',
		'https://github.com/WuAlin0327',
		'https://www.luffycity.com/study'
	]
	p = Pool(2)
	for url in url_list:
		p.apply_async(get_url,args=(url,),callback=call_back)
	p.close()
	p.join()

