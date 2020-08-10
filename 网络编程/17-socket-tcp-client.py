# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-21 08:47:59
# @File_Name: 17-socket-tcp-client.py

from socket import *

# 1.创建套接字
tcpClientSocket = socket(AF_INET, SOCK_STREAM)

# 2.connect() 连接到远程服务器
ipaddr = ('192.168.100.65', 8081)
tcpClientSocket.connect(ipaddr)
print("已连接到tcp服务器...")

# 3. 接收/发送tcp数据
tcpClientSocket.send("Hello Python!!!".encode('gb2312'))
try:
	while True:
		recvData = tcpClientSocket.recv(1024)
		if len(recvData) > 0:
			print("接收到来自%s的数据: %s" % (str(ipaddr), 
				recvData.decode('gb2312')))
		else:
			print("服务端已关闭...")
			break
finally:
	tcpClientSocket.close()
			