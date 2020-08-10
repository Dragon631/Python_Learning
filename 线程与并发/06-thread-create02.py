import threading

class SubThread(threading.Thread):
    def __init__(self, max):
        super().__init__()
        self.max = max
    # 重写run()方法作为线程执行体
    def run(self):
        for i in range(self.max):
            # 调用threading模块current_thread()函数获取当前线程
            # 线程对象的getName()方法获取当前线程的名字
            print(threading.current_thread().getName() +  " " + str(i))
    
# 下面是主程序（也就是主线程的执行体）
for i in range(10):
    # 调用threading模块current_thread()函数获取当前线程
    print(threading.current_thread().getName() +  " " + str(i))
    if i == 2:
        # 创建并启动第一个线程
        t1 = SubThread(5)
        t1.start()
        # 创建并启动第二个线程
        t2 = SubThread(5)
        t2.start()
print('主线程执行完成!')