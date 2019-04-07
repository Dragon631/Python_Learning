#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pickle

str = "Hello world!"

# pickle.dumps 返回一个序列化后的对象，作为字节对象bytes objects
pkd = pickle.dumps(str)
print(pkd)

# pickle.loads 序列化数据转成字符串
pkl = pickle.loads(pkd)
print(pkl)

# pickle.dump 序列化对象，并将其写入文件对象中
# f = open('pkdFile.txt', 'wb')
# pickle.dump(str, f)
# f.close()

# 使用 "with open... as ...:"的好处是不用关闭文件
with open('pkdFile.txt', 'wb') as wbf:
    pickle.dump(str, wbf)

# pickle.load 反序列化对象，将文件中的数据解析为一个python对象
# f = open('pkdFile.txt', 'rb')
# result = pickle.load(f)
# print(result)
with open('pkdFile.txt', 'rb') as wbf:
    data = pickle.load(wbf)
    print(data)