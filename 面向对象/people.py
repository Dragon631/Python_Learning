#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Company(object):
    memberNum = 0
    def __init__(self, name, sex, job, age):
        self.name = name
        self.sex = sex
        self.job = job
        self.age = age
        self.welcome()
    def welcome(self):
        Company.memberNum += 1
        print("Hello %s, Welcome to CGNFex Ltd. Co. The company has [%s] people" % (self.name, self.memberNum))

class Boss(Company):
    def __init__(self, name, sex, job, age, meeting, project):
        super(Boss, self).__init__(name, sex, job, age)
        self.meeting = meeting
        self.project = project

    def what(self):
        print("Boss [%s] have a meeting of [%s] for project [%s]." % (self.name, self.meeting, self.project))

class Staff(Company):
    def __init__(self, name, sex, job, age, working, money):
        super(Staff, self).__init__(name, sex, job, age)
        self.working = working
        self.money = money

    def saysomething(self):
        print("Staff [%s] working for [%s] by [%s]." %(self.name,self.money,self.working))

b = Boss('Shirley','F','Manager',33, 'Sales', 'develop new product')

s = Staff('Saler', 'M', 'Saler', 23, 'Sales', 'Sale products')

b.what()
s.saysomething()