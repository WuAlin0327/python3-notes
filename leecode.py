# import asyncio
# import random
#
# async def task(n):
# 	wait = random.randint(1,5)
# 	print('start run',wait,n)
# 	await asyncio.sleep(wait)
# 	print('end run',wait,n)
#
#
# async def main():
# 	await asyncio.gather(*[task(n) for n in range(10)])
#
# asyncio.run(main())

# import requests
# import asyncio
# import time
#
# async def get_url(url):
# 	print('开始抓取')
# 	res = requests.get(url)
# 	if res.status_code == 200:
# 		return {
# 			'url':url,
# 			'text':len(res.text)
# 		}
#
# async def main():
# 	url_list = [
# 		'https://cloud.tencent.com/developer/article/1194415',
# 		'https://www.cnblogs.com/wualin/',
# 		'https://www.luffycity.com/study',
# 		'https://github.com/WuAlin0327'
# 	]
# start = time.time()
# asyncio.run(main())
# end = time.time()
# print(end-start)
# from gevent import monkey;monkey.patch_all()
# import requests
# import time
# import gevent
# import random
# def get_url(url):
# 	print('开始抓取')
# 	res = requests.get(url)
# 	if res.status_code == 200:
# 		return url,res.text
#
# if __name__ == '__main__':
# 	start = time.time()
# 	url_list = [
# 		'https://cloud.tencent.com/developer/article/1194415',
# 		'https://www.cnblogs.com/wualin/',
# 		'https://www.luffycity.com/study',
# 		'https://github.com/WuAlin0327'
# 	]
# 	g_lis = []
# 	for url in url_list:
# 		g = gevent.spawn(get_url,url)
# 		g_lis.append(g)
#
# 	for g in g_lis:
# 		url,text = g.get()
# 		print(url,len(text))
# 	end = time.time()
# 	print(end-start)


name = 'miao'
age = 123
print('姓名:%s 年龄:%s'%(name,age))