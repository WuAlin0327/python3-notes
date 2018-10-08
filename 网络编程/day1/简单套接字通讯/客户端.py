import socket


#实例化一个socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#

#发起链接
s.connect(('127.0.0.1',8080)) #第一个是绑定的ip地址，第二个是绑定端口

# 发，收消息
s.send('hello'.encode('utf-8'))
data = s.recv(1024)#收到数据最大字节

print(data)
s.close()