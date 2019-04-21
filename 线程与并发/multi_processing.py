# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     multi_processing
   Description :
   Author :       a
   date:          2019/4/15
-------------------------------------------------
"""

# -*- multiprocessing 【案例1】-*- #
# 说明：multiprocessing模块为子进程中运行任务、通信和共享数据，
# 以及执行各种形式的同步提供支持。
# 以单独进程的形式创建和启动函数（或其他可调用对象）
""" 
# 进程类描述：Process([group [, target [, name [, args[, kwargs]]]]])
# group参数未使用，值为None
# targe是当进程启动时执行的可调用对象
# name是为进程制定描述性名称的字符串
# args是传递给target的位置参数的元组
# kwargs是传递给target的关键字参数的字典
import multiprocessing
import time

def clock(interval):
    while True:
        print("The time is %s" % time.ctime())
        time.sleep(interval)

if __name__ =="__main__":
    p = multiprocessing.Process(target=clock, name='test111', args=(3,))  # args参数须为元组类型
    p.start() #启动进程，运行代表进程的子进程，并调用该子进程中的p.run()函数
    n = p.name
    print("%s starting ..." % n)
"""

# -*- multiprocessing 【案例2】-*- #
# 说明：
# 将进程定义为继承自Process的类
# p.run()是进程启动时运行的方法，默认情况下会调用传递给Process构造函数的target方法
# 定义进程的另一种方法是继承Process类并重新实现run()函数
"""
import multiprocessing
import time
class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        # multiprocessing.Process.__init__(self) # 经典写法
        # super(multiprocessing.Process, self).__init__()  # 新型写法
        super().__init__()  # python3 新型写法：super().xxx xxx为父类方法或属性
        self.interval = interval

    def run(self): # 必须重写run()方法，否则将无法运行
        while True:
            print('The time is %s' % time.ctime())
            time.sleep(self.interval)

if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()

# 为了实现跨平台的可移植性，只能像以上方式由主程序创建新的进程
# 这在Unix上可选，但Windows上是必须的
"""

# -*- multiprocessing 【案例3】-*- #
# 说明：
# 进程间通信：管道和队列
# 以下例子说明如何建立永远运行的进程，使用和处理队列上的项目
# 生产者将项目放入队列，并等待它们被处理
"""
import multiprocessing

def consumer(input_q):
    while True:
        item = input_q.get()
        # 处理项目
        print(item) # 此处替换为有用的工作
        # 发出信号通知任务完成
        input_q.task_done()

def producer(sequence, output_q):
    for item in sequence:
        # 将项目放入队列
        output_q.put(item)

# 建立进程
if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    # 运行消费（使用）者进程
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.daemon=True
    cons_p.start()

    # 生产项目，sequence代表要发送给消费者的项目序列
    # 在实践中，这可能是生成器的输出或通过一些其他方式生产出来
    sequence = [1, 2, 3, 4]
    producer(sequence, q)

    # 等待所有项目被处理
    q.join()
    # q.join() 生产者使用此方法进行阻塞，直到队列中的所有项目均被处理。
    # 阻塞将持续到为队列中的每个项目均调用 q.tack_done()方法位为止。
"""

# -*- multiprocessing 【案例4】-*- #
# 说明：
# 如果需要，可以在同一个队列中放置多个进程，
# 也可以从同一个队列中获取多个进程；
# 编写这类代码是，要把队列中的每个项目都序列化，
# 然后通过管道或者套接字连接发送；
# 一般规则是：发送数量较少的大对象比发送大量小对象更好。
"""
import multiprocessing

def consumer(input_q):
    while True:
        item = input_q.get()
        # 处理项目
        print(item) # 此处替换为有用的工作
        # 发出信号通知任务完成
        input_q.task_done()

def producer(sequence, output_q):
    for item in sequence:
        # 将项目放入队列
        output_q.put(item)

# 建立进程
if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    # 启动一些消费（使用）者进程
    cons_p1 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p1.daemon=True
    cons_p1.start()

    cons_p2 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p2.daemon=True
    cons_p2.start()

    # 生产项目，sequence代表要发送给消费者的项目序列
    # 在实践中，这可能是生成器的输出或通过一些其他方式生产出来
    sequence = [1, 2, 3, 4]
    producer(sequence, q)

    # 等待所有项目被处理
    q.join()
"""

# -*- multiprocessing 【案例5】-*- #
# 说明：
# 在某些应用程序中，生产者需要通知使用者，
# 他们不再生产任何项目而且应该关闭
# 为此，编写的代码中应该使用标志（sentinel）——指示完成的特殊值。
# 以下使用None作为标志说明这个概念：
"""
import multiprocessing, os

def consumer(input_q):
    while True:
        item = input_q.get()
        if item is None:
            break
            # 处理项目
        print(item) #替换为有用的工作
    # 关闭
    print("PID %s Consumer done." % os.getpid())

def producer(sequence, output_q):
    print("PID %s producer start." % os.getpid())
    for item in sequence:
        # 把项目放入队列
        output_q.put(item)


if __name__ == '__main__':
    q = multiprocessing.Queue()
    # 启动使用者进程
    cons_p1 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p1.start()
    cons_p2 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p2.start()
    cons_p3 = multiprocessing.Process(target=consumer, args=(q,))
    cons_p3.start()

    print("PPID:", os.getppid())
    # 生产项目
    sequence = [1, 2, 3, 4]
    producer(sequence, q)

    # 在队列上安置标志，发出完成信号
    q.put(None)

    sequence = [5, 6, 7, 8]
    producer(sequence, q)
    q.put(None)

    sequence = ['a', 'b', 'c', 'd']
    producer(sequence, q)
    q.put(None)
    # 等待使用者进程关闭
    # q.join() 生产者使用此方法进行阻塞，直到队列中的所有项目均被处理。
    # 阻塞将持续到为队列中的每个项目均调用 q.tack_done()方法位为止。
    cons_p1.join()
    cons_p2.join()
    cons_p3.join()

# 为每个使用者上都安置标志，如果有三个使用者进程使用队列上的项目
# 则生产者需要在队列上安置三个标记，才能让所有使用者都关闭
"""

# -*- multiprocessing 【案例6】-*- #
# 说明：
# 使用管道在进程之间执行消息传递
# 以下例子说明如何使用管道实现前面的生产者-使用者问题：
"""
import multiprocessing

def consumer(pipe):
    output_p, input_p = pipe
    input_p.close()  # 关闭管道的输入端
    while True:
        try:
            item = output_p.recv()
        except EOFError:
            break
        # 处理项目
        print(item) # 替换为有用的工作
    # 关闭
    print("Consumer done.")

# 生产项目并将器放置到队列上，sequence是代表要处理项目的可迭代对象
def products(sequence, input_p):
    for item in sequence:
        #将项目放在队列上
        input_p.send(item)


if __name__ == '__main__':
    (output_p, input_p) = multiprocessing.Pipe()
    # 启动使用者进程
    cons_p = multiprocessing.Process(target=consumer, args=((output_p,input_p),))
    cons_p.start()

    # 关闭生产者的输出管道
    output_p.close()

    # 生产项目
    sequence = [1, 2, 3, 4]
    products(sequence, input_p)

    # 关闭输入管道，表示完成
    input_p.close()

    # 等待使用者进程关闭
    cons_p.join()
    
# 注意管道端点的管理问题：
# 如果生产者或消费者中都没有使用管道的某个端点，就应将其关闭。
"""

# -*- multiprocessing 【案例7】-*- #
# 说明：
# 管道可用于双向通信
"""
# 利用通常在客户端/服务器计算中使用的请求/响应模型或远程过程调用
# 就可以使用管道编写与程序交互的程序
# adder()函数以服务器的形式运行，等待消息到达管道的端点
# 收到之后，它会执行一些处理并将结果发回改管道
# 注意：send()和recv()方法使用pickle模块对对象进行序列化

import multiprocessing

def adder(pipe):
    # 服务器处理
    server_p, client_p = pipe
    client_p.close()
    while True:
        try:
            x,y = server_p.recv()
        except EOFError:
            break
        result = x + y
        server_p.send(result)
    # 关闭
    print("Server done")

if __name__ == '__main__':
    (server_p, client_p) = multiprocessing.Pipe()
    # 启动服务器进程
    adder_p = multiprocessing.Process(target=adder, args=((server_p, client_p),))
    adder_p.start()

    # 关闭客户端中的服务器管道
    server_p.close()
    client_p.send((3, 4))
    print(client_p.recv())

    # 在服务器上提出一些请求
    client_p.send(('hello','world'))
    print(client_p.recv())

    # 完成，关闭管道
    client_p.close()
    # 等待消费者进程关闭
    adder_p.join()
"""

# -*- 进程池 【案例8】-*- #
# 说明：
# 可以把各种数据处理任务都提交给进程池
# 进程池提供的功能有点类似于列表解析和功能行编程操作（如映射-规约）提供的功能
# 以下例子说明如何使用进程池构建字典，将整个目录中文件的文件名映射为SHA512摘要值
"""
# 创建进程池：
# Pool([numprocess [, initializer [, initargs]]])
# numprocess - 进程数，省略此参数，将使用cpu_count()的值
# initializer - 每个工作进程启动时要执行的可调用对象，默认为None
# initargs - 传递给initializer的参数元组

import os
import hashlib
import multiprocessing

BUFSIZE = 8192  # 读取缓冲区大小
POOLSIZE = 2  # 工作进程的数量


# 生产文件名SHA512摘要值
def comput_digest(filename):
    try:
        f = open(filename, "rb")
    except IOError:
        return None
    digest = hashlib.sha512()
    while True:
        chunk = f.read(BUFSIZE)
        if not chunk: break
        digest.update(chunk)
    f.close()
    return filename, digest.digest()


def build_digest_map(topdir):
    digest_pool = multiprocessing.Pool(POOLSIZE)
    # 使用生成器表达式指定一个目录中的所有文件的路径名称序列
    allfiles = (os.path.join(path, name)
                for path, dirs, files in os.walk(topdir)
                for name in files)
    # imap_unordered()函数将allfiles序列分割并传递给进程池
    # 每个池工作进程使用（调用）compute_digest()函数为它的文件计算SHA512摘要值
    # 结果发回给生成器，然后收集到python字典中
    digest_map = dict(digest_pool.imap_unordered(comput_digest, allfiles, 20)) # 返回迭代器(生成器)
    digest_pool.close()
    return digest_map


# 尝试按照需要修改目录名称
if __name__ == '__main__':
    digest_map = build_digest_map("D:\\test1\\test2\\test3")
    print(len(digest_map))
    for i in digest_map:
        print("文件名：%s\nSHA512值:%s" % (i, digest_map[i]))

# 要记住：
# 只有充分利用了池工作进程才能够使额外的通信开销变得有价值，使用进程池才有意义。
# 一般而言，对于简单的计算（如两个数相加），使用进程池是没有意义的。
"""


# -*- 进程池 【案例9】-*- #
# 说明：
# 共享数据与同步
# 通常，进程之间彼此是完全孤立的，唯一的通信方式是队列过管道。
# 但可以使用两个对象来表示共享数据
# 这些对象使用了共享内存（mmap模块）使访问多个进程成为可能

# 使用共享数组代替管道，将一个由浮点数组成的Python列表发送给另外一个进程
"""
# Value(typecode, arg1, ... argN, lock) 在共享内存中创建ctypes对象
# typecode - 包含array模块使用的相同类型代码（如'i','d'等）的字符串
#	或来自ctypes模块的类型对象（如ctype.c_int, ctype.c_double等）
# arg1, ... argN 将传递给指定类型的构造函数
# lock - 只能使用关键字调用的参数，默认为True，将创建一个新的锁定来包含对值的访问
#   如果传入一个现有锁定，比如Lock或Rlock示例，改锁将用于进行同步
# 如果v是Value创建的共享值的实例，则读取v.value将获取值，赋值v.value将修改值

# Array(typecode, initializer, lock) 在共享内存中创建ctypes数组
# initializer 设置数组初始大小的整数或项目序列，其值和大小用于初始化数组

# RawArray(typecode, initializer) 同Array，但不存在锁定

import multiprocessing

class FloatChannel(object):
    def __init__(self, maxsize):
        #在共享内存中创建一个ctypes数组
        #     typecode_to_type = {
        # 'c': ctypes.c_char,  'u': ctypes.c_wchar,
        # 'b': ctypes.c_byte,  'B': ctypes.c_ubyte,
        # 'h': ctypes.c_short, 'H': ctypes.c_ushort,
        # 'i': ctypes.c_int,   'I': ctypes.c_uint,
        # 'l': ctypes.c_long,  'L': ctypes.c_ulong,
        # 'f': ctypes.c_float, 'd': ctypes.c_double
        # }
        self.buffArr = multiprocessing.RawArray('d', maxsize)
        #在共享内存中创建ctypes对象
        self.buffVal = multiprocessing.Value('i')
        #定义一个信号量1代表：empty
        self.empty = multiprocessing.Semaphore(1)
        #定义一个信号量0代表：full
        self.full = multiprocessing.Semaphore(0)

    def send(self, values):
        #只在缓存为null时继续
        #acquire()会阻塞线程，直到release被调用
        self.empty.acquire()
        nitems = len(values)
        print("保存内容的长度", nitems)
        #设置缓冲区大小
        self.buffVal.value = nitems
        #将值复制到缓冲区中
        self.buffArr[:nitems] = values
        print("缓冲：", self.buffArr[:nitems])
        #发信号通知缓冲区已满
        self.full.release()

    def recv(self):
        #只在缓冲区已满时继续
        self.full.acquire()
        #复制值
        values = self.buffArr[:self.buffVal.value]
        #发送信号，通知缓冲区为空
        self.empty.release()
        return values

#性能测试，接受多条消息
def consume_test(count, ch):
    for i in range(count):
        values = ch.recv()
        print("接收：", values)

#性能测试，发送多条消息
def produce_test(count, values, ch):
    for i in range(count):
        print("发送：", values)
        ch.send(values)


if __name__ == "__main__":
    ch=FloatChannel(100000)
    p = multiprocessing.Process(target=consume_test, args=(10, ch))
    p.start()
    values = [float(x) for x in range(10)]
    produce_test(10, values, ch)
    p.join()
    print("done")
"""

# -*- 托管对象 【案例10】-*- #
# 说明：
# 进程不支持共享
# 创建共享值和数组，只属于一般的python对象
# 而对于更高级的python对象（如字典，列表或用户定义类的实例）不起作用
# 但可以使用管理器实现访问共享对象
# 管理器是独立的子进程（真是的对象），以服务器的形式运行，
# 其他进程通过使用代理访问共享对象，这些对象作为管理服务器的客户端运行
# 使用简单托管对象的最直观方式是使用Manager()函数
# Manager() 在一个单独的进程中创建运行的管理器
# Manage()函数返回的SyncManager的示例m具有一系列方法，可用于创建共享对象，
# 并返回用于访问这些共享对象的代理。
# 通常，可以创建一个管理器，并在启动任何新进程之前使用这些方法创建共享对象。

# 以下实例使用管理器创建一个在进程之间共享的字典
"""
import multiprocessing
import time


# 只要设定要传递的时间，就打印d

def watch(d, evt):
    while True:
        evt.wait()
        print(d)
        evt.clear()


if __name__ == '__main__':
    # 创建运行的管理器
    m = multiprocessing.Manager()
    # 在服务器上创建共享的dict实例
    d = m.dict()
    # 在服务器上创建共享的threading.Event实例
    evt = m.Event()

    # 启动监视字典的进程
    p = multiprocessing.Process(target=watch, args=(d, evt))
    p.daemon = True
    p.start()

    # 更新字典并通知监视着
    d['foo'] = 42
    evt.set()
    time.sleep(5)

    # 更新字典并通知监视者
    d['bar'] = 37
    evt.set()
    time.sleep(5)

    # 终止进程和管理器
    p.terminate()
    m.shutdown()
# 主进程中创建并操作了一个共享的字典和事件，运行时将看到子进程打印数据
"""

# -*- 托管对象 【案例11】-*- #
# 说明：
# 实例：为用户定义类创建管理器
"""
# mgrclass.register(typeid [, callable [, proxytype [, exposed [, method_to_typeid [,create_method]]]]])
# 使用管理器类注册一种新的数据类型
# typeid时一个字符串，用于命名特定类型的共享对象
# callable时创建或返回要共享的实例的可调用对象
# proxytype是一个类，负责提供客户端中要使用的代理对象的实现
# exposed时共享对象上方法名称的序列，它将会公布给代理对象, None/proxytype._exposed
# method_to_typeid是从方法名称到类型IDS的映射，None/proxytype._method_to_typeid
# create_method是一个布尔标志，用于指定是否在mgrclass中创建名为typeid的方法，默认True

import multiprocessing
from multiprocessing.managers import BaseManager

class A(object):
    def __init__(self, value):
        self.x = value
    def __repr__(self):
        return "A(%s)" % self.x
    def getX(self):
        return self.x
    def setX(self, value):
        self.x = value
    def __iadd__(self, value):
        self.x += value
        return self

class MyManager(BaseManager): pass
MyManager.register("A", A)

if __name__ == '__main__':
    m = MyManager()
    m.start()
    # 创建托管对象，为位于管理器服务器上的A创建了一个实例
    a = m.A(37)
    g1 = a.getX()
    print(type(a))
    print(g1)
    s1 = a.setX(38)
    g2 = a.getX()
    print(g2)

    # 在代理上无法访问特殊方法和以下划线(_)开头的所有方法
    # A.__iadd__(12)
    # 异常：TypeError: __iadd__() missing 1 required positional argument: 'value'
"""

# -*- 托管对象 【案例12】-*- #
# 说明：
# 实例：为用户定义类创建管理器，并正确公开__iadd__()方法
"""
import multiprocessing
from multiprocessing.managers import BaseManager
from multiprocessing.managers import BaseProxy

class A(object):
    def __init__(self, value):
        self.x = value
    def __repr__(self):
        return "A(%s)" % self.x
    def getX(self):
        return self.x
    def setX(self, value):
        self.x = value
    def __iadd__(self, value):
        self.x += value
        return self

class AProxy(BaseProxy):
    # referent上公开的所有方法列表
    _exposed_ = ['__iadd__', 'getX', 'setX']
    # 实现代理的公共接口
    def __iadd__(self, value):
        self._callmethod('__iadd__', (value,))
        return self
    @property
    def x(self):
        return self._callmethod('getX', ())

    @x.setter
    def x(self, value):
        return self._callmethod('setX', (value,))


class MyManager(BaseManager): pass
MyManager.register("A", A, proxytype = AProxy)

if __name__ == '__main__':
    m = MyManager()
    m.start()
    # 创建托管对象，为位于管理器服务器上的A创建了一个实例
    a = m.A(37)
    print(type(a))
    # print(dir(a))
    p = a.__iadd__((12))
    a += 3
    print(p,a)
"""

# -*- 连接 【案例13】-*- #
# 说明：
# 连接
# 实现程序与同一台或位于远程系统的进程进行消息传递
# connections.Client(address [, family [, authenticate [, authkey]]])
# 返回值是Connection对象
# address 元组(hostname, port)
# family 地址格式字符串，'AF_INET'、'AF_UNIX'、'AF_PIPE'
# authentication 布尔标志，指定是否使用摘要身份验证
# authkey是包含身份验证密钥的字符串

# connections.Listener(address [, family [, backlog [, authenticate [, authkey]]]])
# 实现一台服务器，用于侦听和处理Client()函数发出的连接
# backlog是一个整数，默认值为1，当address参数指定一个网络连接时，
# 对应于传递给套接字的listen()方法的值

# 服务器程序实例，复制侦听客户端并实现简单的远程操作（加法）
"""
from multiprocessing.connection import Listener

# Server
serv = Listener(('', 15000), authkey=b'123456')
while True:
    conn = serv.accept()

    while True:
        try:
            x, y = conn.recv()
        except EOFError:
            break
        result = x + y
        conn.send(result)
    conn.close()

# Client
# 创建一个客户端，连接到服务器，然后发送一些消息
from multiprocessing.connction import Client

conn = Client(('localhost', 15000), authkey=b'123456')

conn.send((3, 4))
r = conn.recv()
print(r)

conn.send(('Hello', 'world'))
r = conn.recv()
print(r)

conn.close()
"""

