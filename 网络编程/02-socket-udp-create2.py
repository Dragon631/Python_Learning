# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-12 17:37:35
# @File_Name: 02-socket-udp-create2.py

from socket import *


udpSocket = socket(AF_INET, SOCK_DGRAM)
print(dir(udpSocket))