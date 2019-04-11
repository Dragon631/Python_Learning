#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

ip_port = ('127.0.0.1', 3456)

sk = socket.socket()
sk.connect(ip_port)
sk.sendall(('请占领地球！！！').encode())
server_reply = sk.recv(1024)

print(server_reply.decode())

sk.close()






