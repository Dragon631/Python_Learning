# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-19 15:36:41
# @File_Name: 10-socket-udp广播1.py


import socket, sys

dest = ('<broadcast>', 8081)

# 创建udp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 对这个需要发送广播数据的套接字进行修改设置，否则不能发送广播数据
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# 以广播的形式发送数据到本网络的所有电脑中
s.sendto("Hi".encode('gb2312'), dest)

print("等待对方回复（按ctrl+c退出）")

while True:
    (buf, address) = s.recvfrom(1024)
    print("Received from %s: %s" % (address, buf))