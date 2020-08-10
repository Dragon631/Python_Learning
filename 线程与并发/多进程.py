# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     多进程
   Description :
   Author :       a
   date:          2019/5/28
-------------------------------------------------
"""

"""
from time import sleep
def sing():
    for i in range(5):
        print("正在唱歌--%d--" %i)
        sleep(1)

def dance():
    for i in range(5):
        print("正在跳舞--%d--" %i)
        sleep(1)


if __name__ == '__main__':
    sing()
    dance()



from multiprocessing import Process
from time import sleep
def sing():
    for i in range(5):
        print("正在唱歌--%d--" %i)
        sleep(1)

def dance():
    for i in range(5):
        print("正在跳舞--%d--" %i)
        sleep(1)


if __name__ == '__main__':
    s = Process(target=sing)
    d = Process(target=dance)
    s.start()
    d.start()
    s.join()
    d.join()
    print("happy done!")


from multiprocessing import Pool
import os,time,random

def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d"%(msg,os.getpid()))
    #random.random()随机生成0~1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f"%(t_stop-t_start))

if __name__ == '__main__':

    po=Pool(3) #定义一个进程池，最大进程数3
    for i in range(0,10):
        #Pool.apply_async(要调用的目标,(传递给目标的参数元祖,))
        #每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(worker,(i,))

    print("----start----")
    po.close() #关闭进程池，关闭后po不再接收新的请求
    po.join() #等待po中所有子进程执行完成，必须放在close语句之后
    print("-----end-----")

"""
from multiprocessing import Pool
from time import ctime, time, sleep
import os
import random

"""
def test(num):
    print("%d-pid:%d starting" % (num, os.getpid()))
    start_time = time()
    sleep(1)
    stop_time = time()
    elapsed = stop_time - start_time
    print("%d running time:%s" %(num, elapsed))

if __name__ == '__main__':
    p = Pool(3)
    for i in range(10):
        p.apply_async(test, args=(i,))
    print("--start--")
    p.close()
    p.join()
    print("--stop--")
"""


