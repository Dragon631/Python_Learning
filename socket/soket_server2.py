#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

ip_port = ('127.0.0.1', 3456)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print("server waiting ...")
    while True:
        conn, addr = sk.accept()
        client_data = conn.recv(1024)
        print('Remote_cmd: ', str(client_data, 'utf-8'))
    conn.close()