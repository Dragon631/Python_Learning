# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     tsTserv.py
   Description :
   Author :       a
   date:          2019/4/9
-------------------------------------------------
"""

from socket import *

HOST = 'localhost'
PORT = 1234
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('>#').strip()
    if not data:
        break
    tcpCliSock.send(('%s\r\n' %data).encode())
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        break
    print(data)
    tcpCliSock.close()
