# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     conn_client
   Description :
   Author :       a
   date:          2019/4/17
-------------------------------------------------
"""
# Client
# 连接到服务器，然后发送一些消息
from multiprocessing.connection import Client
import multiprocessing

conn = Client(('localhost', 15000), authkey='12345'.encode())
print("Connect to server ...", multiprocessing.current_process())
conn.send((3, 4))
r = conn.recv()
print(r)

conn.send(('Hello', 'world'))
r = conn.recv()
print(r)

conn.close()


