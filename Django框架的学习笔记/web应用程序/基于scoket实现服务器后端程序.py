import socket

sock = socket.socket()
sock.bind(('127.0.0.1',8081))
sock.listen(5)

while 1:
	print('在等待浏览器的链接')
	conn,addr = sock.accept()
	request = conn.recv(1024)
	print(request)
	#以二进制形式打开.html文件，发送到浏览器端（服务端）
	with open('index.html','rb') as f:
		data = f.read()
	# HTTP/1.1 200 OK 响应头，响应报文
	conn.send((b"HTTP/1.1 200 OK \r\n\r\n%s"%data))
	conn.close()

	"""
	post请求报文：
	b'POST / HTTP/1.1\r\nHost: 127.0.0.1:8081\r\nConnection: keep-alive\r\nContent-Length: 51\r\nCache-Control: max-age=0\r\nOrigin: http://127.0.0.1:8081\r\nUpgrade-Insecure-Requests: 1\r\nContent-Type: application/x-www-form-urlencoded\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nReferer: http://127.0.0.1:8081/\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\nusername=%E5%93%88%E5%93%88%E5%93%88&pwd=miaomidwdw'
	get请求报文
	b'GET / HTTP/1.1\r\nHost: 127.0.0.1:8081\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\n\r\n'

	"""
