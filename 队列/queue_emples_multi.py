import threading
import time
from queue import Queue

img_lists = ['lipei_00006.mp3','lipei_00007.mp3','lipei_00012.mp3','lipei_00014.mp3',
             'lipei_00021.mp3','lipei_00027.mp3','lipei_00028.mp3','lipei_00035.mp3',
             'lipei_00039.mp3','lipei_00044.mp3','lipei_00047.mp3','lipei_00049.mp3',
             'lipei_00057.mp3','lipei_00058.mp3','lipei_00059.mp3','lipei_00061.mp3',
             'lipei_00066.mp3','lipei_00068.mp3','lipei_00070.mp3','lipei_00081.mp3',
             'lipei_00087.mp3','lipei_00104.mp3','lipei_00106.mp3','lipei_00117.mp3',
             'lipei_00123.mp3','lipei_00129.mp3',]

q = Queue(10)

class Music_Cols(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        global img_lists
        global q
        while True:
            try:
                music = img_lists.pop(0)
                q.put(music)
            except IndexError:
                break

class Music_Play(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        global q
        while True:
            if q.not_empty:
                music = q.get()
                print('{}正在播放{}'.format(threading.current_thread(), music))
                time.sleep(5)
                q.task_done()
                print('{}播放结束'.format(music))
            else:
                break


if __name__ == '__main__':
    mc_thread = Music_Cols('music_cols')
    mc_thread.setDaemon(True)       # 设置为守护进程，主线程退出时，子进程也kill掉
    mc_thread.start()               # 启动进程
    for i in range(5):              # 设置线程个数（批量任务时，线程数不必太大，注意内存及CPU负载）
        mp_thread = Music_Play('music_play')
        mp_thread.setDaemon(True)
        mp_thread.start()
    q.join()                        # 线程阻塞（等待所有子线程处理完成，再退出）