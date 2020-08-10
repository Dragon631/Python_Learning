# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-19 09:19:13
# @File_Name: 09-socket-udp广播.py

from socket import *
udpSocket = socket(AF_INET, SOCK_DGRAM)
# dest = ('192.168.100.255', 8081)
dest = ('<broadcast>', 18081)
udpSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
udpSocket.sendto('1:100:Dragon:windows:32:Hello'.encode('utf-8'), dest)
udpSocket.close()