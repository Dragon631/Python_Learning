class RoundTFloat(float):
    def __new__(cls, num):
        num = round(num, 4)
        #return super(Round2Float, cls).__new__(cls, num)
        return float.__new__(RoundTFloat, num)

num = RoundTFloat(3.141592654)
print(num)