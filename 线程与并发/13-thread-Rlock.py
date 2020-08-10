class X:
    #定义需要保证线程安全的方法
    def m () :
        #加锁
        self.lock.acquire()
        try :
            #需要保证线程安全的代码
            ＃...方法体
        #使用finally 块来保证释放锁
        finally :
            #修改完成，释放锁
            self.lock.release()