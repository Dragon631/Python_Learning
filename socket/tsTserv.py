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
创建TCP服务器伪代码：
ss = socket                             # 创建服务器套接字
ss.bind()                               # 套接字与地址绑定
ss.listen()                             # 监听连接
inf_loop:                               # 服务器无线循环
    cs = ss.accept()                    # 接受客户端连接
        comm_loop:                   
            cs.recv()/cs.send()         # 对话（接受/发送）
        cs.close()                      # 关闭客户端套接字
ss.close()                              # 关闭服务器套接字
"""
from socket import *
from time import ctime

HOST = 'localhost'
PORT = 2579
BUFSIZ = 1024
ip_port = (HOST, PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ip_port)
tcpSerSock.listen(5)

while True:
    print("Waiting for connecting...")
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from :', addr)

    while True:
        print("Waiting the data from client...")
        data = tcpCliSock.recv(BUFSIZ).decode()
        if not data:
            break
        tcpCliSock.send(('[%s] %s' %(ctime(), data)).encode())
    tcpCliSock.close()
    tcpSerSock.close()