# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     class_method
   Description :
   Author :       a
   date:          2019/5/7
-------------------------------------------------
"""


class Person(object):
    """docstring for Person"""
    def __init__(self, name, age):
        super(Person, self).__init__()
        self.age = age
        self.name = name
        self._pri_data1 = "private data1"
        self.__pri_data2 = "private data2"

    def _pri_fun1(self):
        # return "This is private function 1, _pri_data1:%s,__pri_data2:%s" % (self._pri_data1, self.__pri_data2)
        # return "%s" % self.__pri_fun2()
        return "Person: _pri_fun1"


    def __pri_fun2(self):
        return "This is private function 2, _pri_data1:%s,__pri_data2:%s" % (self._pri_data1, self.__pri_data2)

    def public_fun(self):
        return self._pri_fun1()

    def __str__(self):
        return "I am %s and I am %d years old. Thanks." % (self.name, self.age)


class China(Person):
    def __init__(self, name, age, sex=1):
        super().__init__(name, age)
        self.name = name
        self.age = age

    # def _pri_fun1(self) :
    #     # return "This is private function 1, _pri_data1:%s,__pri_data2:%s" % (self._pri_data1, self.__pri_data2)
    #     return "%s" % self.__pri_fun2()

    def __pri_fun2(self):
        return "This is private function 2"

a = Person("April", 20)
# print(a.name)
# print(a)
b = China("apple", 35, 0)
# bf1 = b._pri_fun1()
b1 = b.public_fun()
a2 = b._pri_fun1()
p = a._pri_fun1()
print(b1)
print(a2)
# print(bf1)

