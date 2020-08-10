# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-20 10:24:03
# @File_Name: 10-socket-udp广播2.py

from socket import *
 
HOST = '<broadcast>'
PORT = 18081
BUFSIZE = 1024
 
ADDR = (HOST, PORT)
 
udpCliSock = socket(AF_INET, SOCK_DGRAM)
udpCliSock.bind(('', 0))
udpCliSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
    data = input('>')
    if not data:
        break
    print("sending -> %s" % data)
    udpCliSock.sendto(data.encode('gb2312'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print(data)