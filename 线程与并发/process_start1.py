import multiprocessing
import os
def foo(q):
    print('被启动的新进程: (%s)' % os.getpid())
    q.put('Python')
if __name__ == '__main__':
    # 设置使用spawn方式启动进程
    multiprocessing.set_start_method('spawn')
    q = multiprocessing.Queue()
    # 创建进程
    mp = multiprocessing.Process(target=foo, args=(q, ))
    # 启动进程
    mp.start()
    # 获取队列中的消息
    print(q.get())
    mp.join()


    