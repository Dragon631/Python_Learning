import struct
from socket import *
udpSocket = socket(AF_INET, SOCK_DGRAM)
bindAddr = ('192.168.100.160', 69)

# timg.jpg
str1 = '!H8sb5sb'.encode('utf-8')
str2 = 'timg.jpg'.encode('utf-8')
str3 = 'octet'.encode('utf-8')
cmdBuf = struct.pack(str1, 1, str2, 0, str3, 0)

udpSocket.sendto(cmdBuf, bindAddr)

