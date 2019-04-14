# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     multi_threads
   Description :
   Author :       a
   date:          2019/4/10
-------------------------------------------------
"""
import time
import threading


def sayhi(num):
    print("Running on number:%s" % num)
    time.sleep(3)


if __name__ == '__main__':
    t1 = threading.Thread(target = sayhi, args=(1,))  # 生成一个线程
    t2 = threading.Thread(target = sayhi, args=(2,))

    t1.start()
    t2.start()

    print(t1.getName())
    print(t2.getName())
    t2.join()
    print("---main---")
