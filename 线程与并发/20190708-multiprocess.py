# -*- coding: utf-8 -*-
# @Date_Time: 2019-07-08 14:10:26
# @File_Name: 20190708-multiprocess.py

import multiprocessing
import os, time

def read(client):
	print(client.recv())

def write(server):
	server.send("hello Pipe")

def main():
	client, server = multiprocessing.Pipe()
	pool = multiprocessing.Pool(processes=2)
	pool.apply_async(write, (server,))
	pool.apply_async(read, (client,))

	pool.close()
	pool.join()


if __name__ == '__main__':
	main()