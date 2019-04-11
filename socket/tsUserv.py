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
创建UDP服务器伪代码：
ss = socket                             # 创建服务器套接字
ss.bind()                               # 绑定服务器套接字
inf_loop:                               # 服务器无线循环                    
    cs = ss.revefrom()/ss.sendto()      # 关闭（接受/发送）
ss.close()                              # 关闭服务器套接字
"""

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 12579
BUFSIZ = 1024
ADDR = (HOST, PORT)
udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print("Waiting for message...")
    data,addr = udpSerSock.recvfrom(BUFSIZ)
    data = data.decode()
    udpSerSock.sendto(('[%s] %s' % (ctime(), data)).encode(), addr)
    print('...received from and returen to:', ADDR)
udpSerSock.close()