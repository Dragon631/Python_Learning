#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

ip_port = ('127.0.0.1', 1111)

sk = socket.socket()
# sk.connect(ip_port)
sk.bind(ip_port)
sk.listen(5)

while True:
    print("Server waiting ...")
    conn, addr = sk.accept()
    client_data = conn.recv(1024)
    print(str(client_data, 'utf-8'))
    conn.sendall(bytes('请不要回答，请不要回答，请不要回答！！！', 'utf-8'))

    conn.close()






