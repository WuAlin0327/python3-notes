from multiprocessing import Pool

def func(i):

	return i*i

if __name__ == '__main__':
	p = Pool(5)
	res_lis = []
	for i in range(10):
		res = p.apply_async(func,args=(i,))
		res_lis.append(res)

	for res in res_lis:
		print(res.get())# res.get 默认是阻塞的，因为需要接收进程处理的结果，之后接收到结果之后才可以继续执行，所以
							# 所以将进程的返回结果放在一个列表中，然后循环这个列表，再执行get就不会阻塞了
	p.close()
	p.join()