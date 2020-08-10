# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-13 09:08:32
# @File_Name: 02-socket-udp-多线程聊天.py

from socket import *
from threading import Thread
import time


# 接收数据
def recvData():
	while True:
		recvInfo = udpSocket.recvfrom(1024)
		if not recvInfo[0] :
			fmt = "%Y-%m-%d %X"
		else :
			fmt = recvInfo[0].decode('gb2312')
		back_msg = time.strftime(fmt)
		print("\n[%s]%s>>%s" % (time.ctime(), recvInfo[1], back_msg))
		# udpSocket.sendto(back_msg.encode('gb2312'), recvInfo[1])

# 发送数据
def sendData():
	destAddr = (destIP, destPort)
	while True:
		data = input("Data<<")
		udpSocket.sendto(data.encode('gb2312'), destAddr)

flag = False
destIP = ''
destPort = 0
udpSocket = None

# main()函数
def main():
	global udpSocket
	global destIP
	global destPort
	destIP = input("Dest_IP:")
	destPort = int(input("Dest_Port:"))
	udpSocket = socket(AF_INET, SOCK_DGRAM)
	bindAddr = ('', 7788)
	udpSocket.bind(bindAddr)
	ts = Thread(target=sendData)
	tr = Thread(target=recvData)

	ts.start()
	tr.start()

	ts.join()
	tr.join()

# 执行程序
if __name__ == '__main__':
	main()