# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-12 17:37:35
# @File_Name: 01-socket-udp-create1.py

import socket


udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 或者 udpSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print(dir(udpSocket))