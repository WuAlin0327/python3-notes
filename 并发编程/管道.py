from multiprocessing import Pipe,Process

def func(conn1,conn2):
	conn2.close()
	while True:
		try:
			msg = conn1.recv()
			print(msg)
		except EOFError:
			print('子进程结束')
			conn1.close()
			break


if __name__ == '__main__':
	conn1,conn2 = Pipe()
	Process(target=func,args=(conn1,conn2)).start()
	conn1.close()
	for i in range(5):
		conn2.send('吃屎了你')
	conn2.close()
