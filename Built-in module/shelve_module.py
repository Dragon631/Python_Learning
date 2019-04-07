# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     shelve_module
   Description :
   Author :       a
   date:          2019/4/2
-------------------------------------------------
"""
__author__ = 'a'

"""
Shelve是对象持久化保存方法，将对象保存到文件里面，缺省（即默认）的数据存储文件是二进制的
使用时，只需要使用open函数获取一个shelf对象，然后对数据进行增删改查操作，
在完成工作、并且将内存存储到磁盘中，最后调用close函数变回将数据写入文件
"""

import shelve

# """
user_info = {
    'a':['Apple', '123456'],
    'b':['Banana', '123456'],
    'c':['cat', '123456']
}

infoFile = shelve.open('infoDb')
infoFile['info'] = user_info
infoFile.close()

infoFile = shelve.open('infoDb')
data = infoFile['info']
print(type(data))
print(data)

"""

# 自定义类
class Student(object):
    def __init__(self, name, age, sno):
        self.name = name
        self.age = age
        self.sno = sno

    def __repr__(self):
        return 'Student [name: %s, age: %d, sno: %d]' % (self.name, self.age, self.sno)

Tom = Student('Tom', 25, 201901)
Adm = Student('Adm', 21, 201902)
# print(Tom,Adm)

# with shelve.open("info.db") as db:
db = shelve.open("info.db")
db['Tom'] = Tom
db['Adm'] = Adm
db['Adm'] = Adm
db.close()

# with shelve.open("info.db") as db:
db = shelve.open("info.db")
print(db['Tom'])
print(db['Adm'])
print(db.items())
# db.pop('Adm')
db.close()

db = shelve.open("info.db")
print(db['Adm'])
db.close()

"""