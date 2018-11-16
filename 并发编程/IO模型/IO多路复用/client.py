import socket
import time
from threading import Thread

def func():
	sk = socket.socket()
	sk.connect(('127.0.0.1',8080))
	sk.send(b'hello')
	time.sleep(3)
	print(sk.recv(1024))
	sk.close()


if __name__ == '__main__':
	for i in range(20):
		t = Thread(target=func)
		t.start()