#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys


class WebServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        print("Service Starting...")

    def stop(self):
        print("Service Stopping...")

    def restart(self):
        self.stop()
        self.start()


def test_run(self, name):
    print("Running testing...", name, self.host)


if __name__ == "__main__":
    server = WebServer('localhost', 8888)
    """
    存在重复代码，不够优化
    dic = {
        'start': server.start,
        'stop': server.stop,
        'restart': server.restart
    }
    if sys.argv[1] in dic:
        dic[sys.argv[1]]()
    """

    """
    hasattr(object, name)
    判断一个对象里面是否有name变量或者name方法，
    返回BOOL值，有name特性返回True， 否则返回False
    需要注意的是name参数是string类型，所以不管是要判断变量还是方法
    
    getattr(object, name[,default])
    获取的对象是属性，存在就打印出来，如果不存在，打印出默认值，默认值可选；
    如果获取对象是方法，存在就打印出方法的内存地址，后面加括号可以将这个方法运行
    
    setattr(object, name, values)
    给object对象的name属性赋值value，如果对象原本存在给定的属性name，
    则setattr会更改属性的值为给定的value；如果对象原本不存在属性name，
    setattr会在对象中创建属性，并赋值为给定的value；
    
    delattr(object, name)
    函数作用用来删除指定对象的指定名称的属性，和setattr函数作用相反,
    注意，当属性不存在的时候，会报错；不能删除对象的方法
    """
    if hasattr(server, sys.argv[1]):
        func = getattr(server, sys.argv[1])     # 获取server.start/stop/restart内存地址
        func()

    setattr(server, 'run', test_run)
    server.run(server, 'abc')
    # print(server.host)
    # delattr(server, 'host')
    # # server.start()
    # print(server.host)

    # server.start()
    # delattr(WebServer, 'start')
    # server.start()


