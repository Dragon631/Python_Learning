#-*- coding:utf-8 -*-
import threading
import time
"""
# 创建一个线程锁
mylock = threading.Lock()

tickets = range(1,10)
 
def buy_ticket(station):
    while True:
        mylock.acquire()     #加线程锁
        if len(tickets) == 0:
            mylock.release()  #释放线程锁， 不要带锁结束线程
        break
    ticket = tickets[-1]
    time.sleep(1)
    print("%s买到票No.%d" %(station, ticket))
    del tickets[-1]
    mylock.release()      #释放线程锁
    time.sleep(1)
 
class MyThread(threading.Thread):
    def __init__(self, station):
        threading.Thread.__init__(self)
        self.station = station
        #线程启动后，会执行self.run()方法
    def run(self):
        buy_ticket(self.station)
 

 
# 创建新线程t1
t1 = MyThread("广州")
t2 = MyThread("深圳")
 
t1.start()    #启动线程
t2.start()
print("线程启动完毕")
 
print('end.')

"""

def foo():
    global num
    if s.acquire():
        print("get num:%s"%num)
        num -= 1
        time.sleep(1)
        s.release()
    print("result:%s" % threading.active_count())


# lock = threading.Semaphore(2)
num = 10
l = list()
s = threading.BoundedSemaphore(2)
for i in range(10):

    t = threading.Thread(target=foo)
    t.start()
    l.append(t)

for j in l:
    j.join()

