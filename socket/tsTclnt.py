# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     tsTserv.py
   Description :
   Author :       a
   date:          2019/4/9
-------------------------------------------------
"""
"""
创建TCP客户端伪代码：
cs = socket                     # 创建客户端套接字
cs.connect()                    # 尝试连接服务器                 # 接受客户端连接
comm_loop:                   
    cs.recv()/cs.send()         # 对话（接受/发送）
cs.close()                      # 关闭客户端套接字
"""
from socket import *

HOST = 'localhost'
PORT = 2579
BUFSIZ = 1024
ip_port = (HOST, PORT)
# tcpCliSock = socket.socket()
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ip_port)

while True:
    data = input('>')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        break
    print(data)
tcpCliSock.close()
