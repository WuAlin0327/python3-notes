import socket

#实例化一个socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#

#绑定ip地址
s.bind(('127.0.0.1',8080)) #第一个是绑定的ip地址，第二个是绑定端口 0-65535:0-124

#监听
s.listen(5) #最大挂起的链接数

#等待链接
conn,client_addr = s.accept()#conn相当于传输层的管道

# 收，发消息
data = conn.recv(1024)#接收数据的最大限制 单位：bytes
print('客户端的数据',data)

conn.send(data.upper())

conn.close()
s.close()
