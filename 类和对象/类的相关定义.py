#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys

class Server(object):
    def __init__(self, host, port, service):
        self.host = host
        self.port = port
        self.service = service

    def start(self):
        print("%s starting ..." % self.service)

    def stop(self):
        print("%s stopping ..." % self.service)

    def restart(self):
        self.stop()
        self.start()

def run_custom(self):
    print('%s is running...'%self.host)



if __name__ == "__main__":

    webserver = Server('localhost', 443, 'httpd')

    if hasattr(webserver, sys.argv[1]):
        fun = getattr(webserver, sys.argv[1])
        fun()


    setattr(webserver, 'run', run_custom)

    webserver.run(webserver)
    print(webserver.host)