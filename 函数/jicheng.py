# -*- coding: utf-8 -*-

class D:
    def __init__(self):
        self.n = "D"

class E:
    def __init__(self):
        self.n = "E"

class B(D):
    def __init__(self):
        super().__init__()
        self.n = "B"

class C(E):
    def __init__(self):
        super().__init__()
        self.n = "C"

class A(B, C):
    def __init__(self):
        super().__init__()
        self.n = "A"

a = A()
print(a.n)
print(A.mro())