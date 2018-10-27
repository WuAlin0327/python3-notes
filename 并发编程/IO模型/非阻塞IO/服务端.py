from socket import *

server = socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8090))
server.listen(5)
server.setblocking(False)
print('strting...')
rlist = []
while True:
	try:
		conn,addr = server.accept()
		rlist.append(conn)

	except BlockingIOError:
		pass