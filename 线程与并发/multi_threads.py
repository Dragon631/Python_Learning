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

"""
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
"""

class ClockThread(threading.Thread):
    def __init__(self,interval):
        # threading.Thread.__init__(self) # 必须调用基类的构造函数，否则将导致严重错误
        super().__init__()
        self.interval = interval
        self.daemon = True

    def run(self):
        while True:
            print("Current time %s" % time.ctime())
            time.sleep(self.interval)

if __name__ == '__main__':
    t1 = ClockThread(3)
    t1.start()
    t2 = ClockThread(3)
    t2.start()
    t2.join()


