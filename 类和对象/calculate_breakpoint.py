# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     calculate_breakpoint
   Description :
   Author :       a
   date:          2019/5/7
-------------------------------------------------
"""
def sum(a, b):
    t = a + b
    print(t)

def div(a, b):
    t = a/b
    print(t)

def total():
    sum = 1
    for i in range(1,31):
        if i == 1:
            sum = 1
        else:
            sum += sum*2
        print("%d===>%d"%(i, sum))

def total1():
    sum = 1
    t = 1
    for i in range(1,31):
        if i == 1:
            sum = 1
        else:
            t = t * 2
            sum = sum + t
        print("%d==>%d==>%d"%(i, t, sum))

"""
1
3
9
27
81
sum = 

d = 2^n + 2^(n-1)+..2*2+2*1+1

"""

def main():
    a = 6
    b = 3



if __name__ == '__main__':
    a = 123456784525666666666
    b = 123456784525666666666
    print(a == b, a is b)

    s1 = 'Hello'
    s2 = 'Hello World'
    print(s1)


