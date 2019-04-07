#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

ip_port = ('127.0.0.1', 3456)
sk = socket.socket()
sk.connect(ip_port)

while True:
    input_data = input('>># ').strip()
    sk.sendall(bytes(input_data, 'utf-8'))
    # server_reply = sk.recv(1024)
sk.close()