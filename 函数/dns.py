# -*- coding: utf-8 -*-

# import dns.resolver

# 查询A记录
# domain = input("Please input a domain: ")
# A = dns.resolver.query(domain, "A")
# for i in A.response.answer:
#     for j in i.items:
#         if j.rdtype == 1:
#             print(j)


class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

for x in reversed(FloatRange(1.0, 4.0, 0.5)):
    print(x)


