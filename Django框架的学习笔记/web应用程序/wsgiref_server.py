from wsgiref.simple_server import make_server

def callback(environ,start_response):
	# environ是请求报文(wsgiref模块打包成了字典格式)
	path = environ.get('PATH_INFO')
	print(path)
	# start_response是打包响应报头
	start_response('200 OK',[])
	if path == '/index':
		with open('index.html','r') as f:
			data = f.read()
	elif path == '/login':
		with open('login.html','r') as f:
			data = f.read()
			print(data)
	elif path == '':
		data = ''

	return [data.encode('utf-8')]

#建立链接，相当于socket模块中的实例化一个socket对象并且绑定ip端口以及监听
httped = make_server("",8080,callback)

#相当于socket模块中的conn,addr = sock.accept()等待别人来链接，来链接之后调用make_server对象中的回调函数
httped.serve_forever()