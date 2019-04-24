# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     test
   Description :
   Author :       a
   date:          2019/4/21
-------------------------------------------------
"""
"""
import threading
import time
import random


def door():
    door_open_time_counter = 0
    while True:
        if door_swiping_event.is_set():
            print("\033[32;1m door opening....\033[0m")
            door_open_time_counter += 1

        else:
            print("\033[31;1m door closed...., swipe to open.\033[0m")
            door_open_time_counter = 0  # 清空计时器
            door_swiping_event.wait()

        if door_open_time_counter > 3:  # 门开了已经3s了,该关了
            door_swiping_event.clear()

        time.sleep(0.5)


def staff(n):
    print("staff [%s] is coming..." % n)
    while True:
        if door_swiping_event.is_set():
            print("\033[34;1m door is opened, passing.....\033[0m")
            break
        else:
            print("staff [%s] sees door got closed, swiping the card....." % n)
            # print(door_swiping_event.set())
            door_swiping_event.set()
            print("after set ", door_swiping_event.is_set())
        time.sleep(0.5)


if __name__ == "__main__":

    door_swiping_event = threading.Event()  # 设置事件
    door_thread = threading.Thread(target=door)
    door_thread.start()

    for i in range(20):
        p = threading.Thread(target=staff, args=(i,))
        time.sleep(random.randrange(3))
        p.start()
"""

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