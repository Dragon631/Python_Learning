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
# 直接调用多线程
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

"""
# 通过继承调用多线程
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
"""

"""
# 实现员工刷门禁进入公司大门的功能
import time
import random
import threading
event_door_open = threading.Event()
def door():
    if not event_door_open.is_set():
        event_door_open.set()
    count_door_open = 0
    while True:
        if event_door_open.is_set():
            print("\033[42mDoor is open ...\033[0m")
            count_door_open += 1
        else:
            print("\033[41mDoor is close ...\033[0m")
            event_door_open.wait()

        if count_door_open > 3:
            count_door_open = 0
            event_door_open.clear()
        time.sleep(1)

def staff(n):
    print("Staff-[%s] arrived on the door ..." % n)
    while True:
        if event_door_open.is_set():
            print("\033[32mStaff-[%s] access the door ...\033[0m" % n)
            break
        else:
            print("\033[31mDoor is close. Staff-[%s] ready to brush the access card ...\033[0m" % n)
            event_door_open.set()
            print("\033[42mStaff-[%s] is opening the door ...\033[0m" % n)

if __name__ == "__main__":
    d = threading.Thread(target=door)
    d.start()

    for i in range(20):
        p = threading.Thread(target=staff, args=(i,))
        time.sleep(random.randrange(10))
        p.start()
"""

"""
# Event事件实现红绿灯
import threading
import time

event = threading.Event()

def lighter():
    if not event.is_set():
        event.set()
    count = 0
    while True:
        if count < 5:
            print("\033[42mGreen light on ...%s\033[0m." % count)
        elif count < 8:
            print("\033[43mYellow light on ...%s\033[0m." % count)
        elif count < 12:
            if event.is_set():
                event.clear()
            print("\033[41mRed light on ...%s\033[0m." % count)
        else:
            count = 0
            event.set()

        count += 1
        time.sleep(1)

def car(n):
    while True:
        if event.is_set():
            print("\033[32mCar#%s is running ...\033[0m." % n)
        else:
            print("\033[31mCar#%s is waiting for red light ...\033[0m." % n)
            event.wait()
        time.sleep(1)


if __name__ == '__main__':
    l = threading.Thread(target=lighter)
    l.start()
    c1 = threading.Thread(target=car, args=("1",))
    c2 = threading.Thread(target=car, args=("2",))
    c3 = threading.Thread(target=car, args=("3",))
    c1.start()
    c2.start()
    c3.start()
"""

"""
# Semaphore([value])
# value为计数器初始值，省略参数则将值置为1
# 每次调用acquire()方法时，计数器减1；每次调用release()方法时，计数器加1
# 计数器为0时，acquire()方法将阻塞，直到其他线程调用release()方法为止

import threading
import time
import random

semaphore = threading.Semaphore(0)

def consumer():
    print("consumer is waiting.")
    semaphore.acquire()
    print("Consumer notify: consumed item number %s." % item)

def producer():
    global item
    time.sleep(2)
    item = random.randint(1, 1000)
    print("producer nofity: produced item number %s." % item)
    semaphore.release()



if __name__ == "__main__":

    for i in range(0, 5):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    print("program teminated.")
"""

import threading, time


def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("Active_count: %d, Run the thread:%d => %d" % (threading.active_count(),threading.get_ident(),n))
    semaphore.release()


if __name__ == '__main__':

    num = 0
    semaphore = threading.BoundedSemaphore(2)

    for i in range(1,21):
        # time.sleep(1)
        t = threading.Thread(target=run, args=(i,))
        t.start()

while threading.active_count() != 1:
    pass
else:
    print("---------all threads done---------")

