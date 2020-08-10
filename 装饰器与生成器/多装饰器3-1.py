# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     多装饰器3
   Description :
   Author :       a
   date:          2019/4/10
-------------------------------------------------
"""


def wrapper_A(func):
    print('----A1----')
    def inner1():
        print("----11----")
        return "<A>" + func() + "</A>"
    print("----A2----")
    return inner1


def wrapper_B(func):
    print('----B1----')

    def inner2():
        print("----21----")
        return "<B>" + func() + "</B>"
    print("----B2----")
    return inner2

@wrapper_A
@wrapper_B
def test():
    # print("#--test--#")
    return "Hello Wrapper"

# test = wrapper_A(wrapper_B(test))

if __name__ == '__main__':
    print(test())


"""
----B1----
----B2----
----A1----
----A2----
----11----
----21----
<A><B>Hello Wrapper</B></A>
"""