#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

ip_port = ('127.0.0.1', 3456)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
	print("server waiting ...")
	conn, addr = sk.accept()
	#client_data = conn.recv(1024)
	#print(str(client_data,'utf-8'))
	#client_reply = conn.sendall(bytes('Hello Client.', 'utf-8'))
	while True:
		try:
			client_data = conn.recv(1024)
			print('client_reply: ', str(client_data,'utf-8'))
		except Exception:
			print("No client response")
			break
		server_data = input("Server# ").strip()
		server_replay = conn.sendall(bytes(server_data,'utf-8'))
	conn.close()