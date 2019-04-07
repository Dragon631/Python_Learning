#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

ip_port = ('192.168.100.65', 3456)

sk = socket.socket()
sk.connect(ip_port)
sk.sendall(bytes('请占领地球！！！', 'utf-8'))
server_reply = sk.recv(1024)

print(str(server_reply, 'utf-8'))

sk.close()






