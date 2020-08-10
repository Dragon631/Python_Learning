# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-20 10:37:35
# @File_Name: 09-socket-udp广播-client.py

import socket

'''
客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据：
'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
PORT = 9999
network = '<broadcast>'
# 发送数据:
s.sendto(u"有新文件到达，请登录http://192.168.1.2:8080查看".encode("gb2312"), (network, PORT))

s.close()