# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     basic_test
   Description :
   Author :       a
   date:          2019/4/10
-------------------------------------------------
"""
# 创建一个house类和bed类
# 为house对象添加bed对象
#
# 定义 House 类
class House(object):
    def __init__(self, area, name):
        self.area = area
        self.name = name
        self.left_area = area
        self.item_list = []

    def __str__(self):
        return "户型：%s，总面积：%d m^2，所剩面积：%d, 家具：%s" % (self.name, self.area, self.left_area, str(self.item_list))

    def add_item(self, item):
        # self.left_area -= item.area
        # self.item_list.append(item.name)

        if self.left_area <= item.get_area():
            return

        self.left_area -= item.get_area()
        self.item_list.append(item.get_name())

# 定义 Bed 类
class Bed(object):
    __instance = "A"
    def __init__(self, area, name):
        self.area = area
        self.name = name

    def __str__(self):
        return "样式：%s，面积：%d m^2" % (self.name, self.area)

    def get_area(self):
        return self.area

    def get_name(self):
        return self.name

    def hello(self):
        return "Hello everybody..." + Bed.staticm()

    @classmethod
    def classm(cls):
        return "Hi %s, I'm classmethod..." % Bed.__instance

    @staticmethod
    def staticm():
        return "I'm staticmethod..."


h1 = House(115, '三室两厅')
print(h1)

b1 = Bed(114, '双人床')
print(b1)
print(b1.classm())
print(b1.staticm())
print(b1.hello())

h1.add_item(b1)
h1.add_item(b1)
h1.add_item(b1)
print(h1)