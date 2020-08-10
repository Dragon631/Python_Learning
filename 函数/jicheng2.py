class Init(object):
    def __init__(self,v):
        print("init")
        self.val = v
class Add2(Init):
    def __init__(self,val):
        print("Add2")
        super().__init__(val)
        print(self.val)
        self.val += 2
class Mult(Init):
    def __init__(self,val):
        print("Mult")
        super().__init__(val)
        self.val *= 5
class HaHa(Init):
    def __init__(self,val):
        print("HaHa")
        super().__init__(val)
        self.val /= 5
class Pro(Add2,Mult,HaHa):
    def __init__(self, val) :
        print("pro")
        super().__init__(val)
        self.val /= 5
class Incr(Pro):
    def __init__(self,val):
        super().__init__(val)
        self.val += 1
p = Incr(5)
print(p.val)
