import socket
import select

sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.setblocking(False)
sk.listen(5)

read_lst = [sk]

while True:
	r_lst,w_lst,x_lst = select.select(read_lst,[],[])
	for i in r_lst:
		if i is sk:
			conn,addr = i.accept()
			read_lst.append(conn)
		else:
			ret = i.recv(1024)
			if ret == b'':
				i.close()
				read_lst.remove(i)
				continue
			print(ret)
			i.send(b'goodbye!')
