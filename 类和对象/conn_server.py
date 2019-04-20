# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     conn_server
   Description :
   Author :       a
   date:          2019/4/17
-------------------------------------------------
"""
from multiprocessing.connection import Listener
import multiprocessing
# Server
serv = Listener(('', 15000), authkey='12345'.encode())
print("Waiting connecttion for client ...", multiprocessing.current_process())
while True:
    conn = serv.accept()
    print("Waiting for next client data...")
    while True:
        try:
            x, y = conn.recv()
        except EOFError:
            break
        result = x + y
        conn.send(result)

    conn.close()

