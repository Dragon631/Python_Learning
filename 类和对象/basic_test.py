# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     basic_test
   Description :
   Author :       a
   date:          2019/4/10
-------------------------------------------------
"""
__author__ = 'a'


class Student(object):
    __count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def sayhi():
        print("Say hi!")

    def info(self):
        Student.__count += 1
        return 'No.%s >> Name: %s, Age: %s' % (self.__count, self.name, self.age)

    def get_name(self):
        return self.name


if __name__ == '__main__':

    s1 = Student('April', 34)
    s2 = Student('Apple', 21)
    # print(s1.info())
    # print(s2.info())
    # print(Student.count)
    # print(s1.__count)
    print(Student.info)
    print(s1.info())
    print(s2.info())


    # print(Student('a',21).info())
    # print(Student('a',21).get_name())
    # print(s1.sayhi())
    # print(s2.__dict__)