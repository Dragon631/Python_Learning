# -*- coding: utf-8 -*-
# @Date_Time: 2019-06-18 09:36:59
# @File_Name: 07-socket-udp-多线程聊天2.py


from socket import *
from threading import Thread
import time

# 接收数据
def recvData():
	while True:
		recvinfo = udpSocket.recvfrom(1024)
		print("%s %s %s \n" % (time.ctime(), recvinfo[1], recvinfo[0].decode('gb2312')))

# 发送数据
def sendData():
	while True:
		data = input("input<<:\n")
		sendMsg = data.encode('gb2312')
		udpSocket.sendto(sendMsg, sendAddr)

udpSocket = None
recvAddr = None
sendAddr = None
# main主函数
def main():
	global sendAddr
	global udpSocket
	global recvAddr
	udpSocket = socket(AF_INET, SOCK_DGRAM)
	recvAddr = ('', 7788)
	sendAddr = ('192.168.100.160', 8081)
	udpSocket.bind(recvAddr)
	ts = Thread(target=sendData)
	tr = Thread(target=recvData)
	ts.start()
	tr.start()

	ts.join()
	tr.join()



# 执行当前脚本
if __name__ == '__main__':
	main()