# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     socketserver_test
   Description :
   Author :       a
   date:          2019/4/9
-------------------------------------------------
"""
__author__ = 'a'

from socketserver import(TCPServer as TCP,
    StreamRequestHandler as SRH)
from time import ctime


HOST = ''
PORT = 1234
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from', self.client_address,
              self.wfile.write('[%s] %s' % (ctime(),
              self.rfile.readline())))

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()
