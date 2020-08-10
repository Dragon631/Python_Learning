# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-21 08:47:59
# @File_Name: 16-socket-tcp-server.py

from socket import *

# 1.创建套接字
tcpSocket = socket(AF_INET, SOCK_STREAM)

# 2.绑定ip-端口
ip_port = ('192.168.100.65', 8081)
tcpSocket.bind(ip_port)

# 3.监听端口，使套接字变为可以被动连接
tcpSocket.listen(5)
print("阻塞1：已准备好被动连接监听，等待客户端连接的到来...")

# 4.accpet() 使套接字等待tcp客户端连接的到来
newSocket, clientAddr = tcpSocket.accept()
print("阻塞2：客户端已连接，等待客户端发送数据...")

# 5. 接收/发送tcp数据
recvData = newSocket.recv(1024)
print("收到来自%s 的信息：%s" % (clientAddr, 
	recvData.decode('gb2312')))

newSocket.send("Hello Python!!!".encode('gb2312'))

newSocket.close()
tcpSocket.close()