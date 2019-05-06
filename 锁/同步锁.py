# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     同步锁
   Description :
   Author :       a
   date:          2019/4/23
-------------------------------------------------
"""
__author__ = 'a'

"""

import threading
import time

mutexA = threading.Lock()
mutexB = threading.Lock()

class MyThreadA(threading.Thread):
    def run(self):
        if mutexA.acquire():
            print("MutexA=>A ... ")
            time.sleep(1)
            if mutexB.acquire(timeout=1):
                print("MutexA=>B ... ")
                mutexB.release()
            mutexA.release()

class MyThreadB(threading.Thread):
    def run(self):
        if mutexB.acquire():
            print("MutexB=>B ... ")
            time.sleep(1)
            if mutexA.acquire(timeout=1):
                print("MutexB=>A ... ")
                mutexA.release()
            mutexB.release()


if __name__ == '__main__':
    a = MyThreadA()
    b = MyThreadB()

    a.start()
    b.start()

"""

"""
# 多线程共享数据（无锁的情况1）

import threading
import time

def sum(n):
    global num
    time.sleep(0.1)
    num -= 1
    # print("Thread-%s, total is :%d" % (n, num))

if __name__ == "__main__":
    t_list = list()
    num = 100
    for i in range(99):
        s = threading.Thread(target=sum, args=(i, ))
        # time.sleep(0.1)
        s.start()
        t_list.append(s)
    for j in t_list:
        j.join()

    print("--------all thread has finished")
    print("num:", num)  # 输出最后的num值
"""


import threading
import time

def foo():
    global num
    time.sleep(1)
    lock.acquire()
    for i in range(10):
        # lock.acquire()
        num += i
        print("Total_foo:%s" % num)
    lock.release()


def bar():
    global num
    time.sleep(1)
    lock.acquire()
    for i in range(10):
        # lock.acquire()
        num += i
        print("Total_bar:%s" % num)
    lock.release()

lock = threading.Lock()
num = 0
f = threading.Thread(target=foo)
b = threading.Thread(target=bar)

f.start()
b.start()
time.sleep(1)
print("--------all thread has finished")
print("num:", num)  # 输出最后的num值
"""
import time,threading

n = 110

def test1():

    global n
    num = 11
    print("局部变量：%s，全局变量：%s" % (num, n))

def test2():
    time.sleep(1)
    global n
    n += 1
    num = 22
    print("局部变量：%s，全局变量：%s" % (num, n))

t1 = threading.Thread(target=test1, args=())
t2 = threading.Thread(target=test2, args=())

t1.start()
t2.start()
"""