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
创建UDP客户端伪代码：
cs = socket                         # 创建客户端套接字
comm_loop:                          # 通信循环
    cs.recvfrom()/cs.sendto()       # 对话（接受/发送）
cs.close()                          # 关闭客户端套接字
"""
from socket import *

HOST = '192.168.100.65'
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)
udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('>')
    if not data:
        break
    udpCliSock.sendto(data.encode(), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    data = data.decode()
    if not data:
        break
    print(data)
udpCliSock.close()
