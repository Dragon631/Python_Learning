# -*- coding=utf-8 -*-
"""
print("*"*10+"FIFO 先进先出队列"+"*"*10)
from queue import Queue  # FIFO 队列
q = Queue(3)  	# 创建队列对象
q.put(0)		# 在队列尾部插入元素
q.put(1)
q.put(2)
print('FIFO队列,', q.queue) # 查看队列中的所有元素
print('第一个元素：', q.get()) # 返回并删除队列头部元素
print(q.queue)

print("\n"+"*"*10+"LIFO 后进先出队列"+"*"*10)
from queue import LifoQueue # LIFO 队列
lifoQueue = LifoQueue()
lifoQueue.put(1)
lifoQueue.put(2)
lifoQueue.put(3)
print('LIFO队列：', lifoQueue.queue)
print('第一个元素：',lifoQueue.get()) # 返回并删除队列尾部元素
lifoQueue.get()
print(lifoQueue.queue) 


print("\n"+"*"*10+"Priority 优先队列"+"*"*10)
from queue import PriorityQueue # 优先队列
priorityQueue = PriorityQueue() # 创建优先队列对象
priorityQueue.put(3)	# 插入元素
priorityQueue.put(78)	# 插入元素
priorityQueue.put(100)	# 插入元素
print(priorityQueue.queue) # 查看优先级队列中的所有元素
priorityQueue.put(1)	# 插入元素
priorityQueue.put(2)	# 插入元素
print('优先级队列：', priorityQueue.queue)
priorityQueue.get()	# 返回并删除优先级最低的元素
print('删除后剩余元素：',priorityQueue.queue)  #删除后剩余元素
priorityQueue.get()	# 返回并删除优先级最低的元素
print('删除后剩余元素：',priorityQueue.queue)  #删除后剩余元素
priorityQueue.get() #返回并删除优先级最低的元素
print('删除后剩余元素：',priorityQueue.queue)  #删除后剩余元素
priorityQueue.get() #返回并删除优先级最低的元素
print('删除后剩余元素：',priorityQueue.queue)  #删除后剩余元素
priorityQueue.get() #返回并删除优先级最低的元素
print('全部被删除后:',priorityQueue.queue)  #查看优先级队列中的所有元素

print("\n"+"*"*10+"deque 双端队列"+"*"*10)
from collections import deque   #双端队列
dequeQueue = deque(['Eric', 'John', 'Smith'])
print('队列元素：', dequeQueue)
dequeQueue.append('Tom')    #在右侧插入新元素
dequeQueue.appendleft('Terry')  #在左侧插入新元素
print(dequeQueue)
dequeQueue.rotate(2)    #循环右移2次
print('循环右移2次后的队列',dequeQueue)
dequeQueue.popleft()    #返回并删除队列最左端元素
print('删除最左端元素后的队列：',dequeQueue)
dequeQueue.pop()    #返回并删除队列最右端元素
print('删除最右端元素后的队列：',dequeQueue)
"""

import queue
import threading
import time

class Worker(threading.Thread):
    def __init__(self, queue):
        super(Worker, self).__init__()
        self.queue = queue
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            print("Thread-%s %s is waiting for task ..." % (self.ident, self.name))
            try:
                task = q.get(block=True, timeout=1)
            except queue.Empty:
                print("Nothing to do, go home.")
                self.thread_stop = True
                break
            print("\033[32mTask:%s, task No.:%d\033[0m" % (task[0], task[1]))
            print("I am working.")
            time.sleep(1)
            print("\033[42mTask:%s Finished.\033[0m" % task[0])
            q.task_done()
            res = q.qsize()
            if res > 0:
                print("Damn it. Still %d task to be doing." % res)

    def stop(self):
        self.thread_stop = True


if __name__ == '__main__':
    q = queue.Queue(3)
    worker = Worker(q)
    worker.start()
    q.put(["Produce CPU.", 1], block=True, timeout=None)
    q.put(["Produce desk.", 2], block=True, timeout=None)
    q.put(["Produce car.", 3], block=True, timeout=None)
    q.put(["Produce mobile.", 4], block=True, timeout=None)
    q.put(["Produce host.", 5], block=True, timeout=None)

    print("waiting for task finish!")
    q.join()
    print("All tasks finished!")




