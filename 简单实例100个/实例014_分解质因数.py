# coding: utf-8
"""
-------------------------------------------------
   File Name:     实例014_分解质因数
   Description :
   Author :       a
   date:          2020/6/1
-------------------------------------------------

题目
    将一个整数分解质因数。例如：输入90,打印出90=233*5。

程序分析
    根本不需要判断是否是质数，从2开始向数本身遍历，能整除的肯定是最小的质数

"""

"""
当迭代对象完成所有迭代后且此时的迭代对象为空时，
如果存在else子句则执行else子句，没有则继续执行后续代码；
如果迭代对象因为某种原因（如带有break关键字）提前退出迭代，
则else子句不会被执行，程序将会直接跳过else子句继续执行后续代码
"""
# 方法1
n = int(input("please input a number: "))
m = n
li = []
s = ''
while True:
    for i in range(2, n+1):
        if n % i == 0:
            li.append(i)
            n = int(n / i)
            break
    else:
        break
# print(li)

for j in range(len(li)):
    if j == (len(li)-1):
        s = s + "*"+str(li[j])
        break
    s += str(li[j])
# print(s)


# 方法2：
target=int(input('输入一个整数：'))
print(target,'= ',end='')

if target<0:
    target=abs(target)
    print('-1*',end='')

flag=0
if target<=1:
    print(target)
    flag=1


while True:
    if flag:
        break
    for i in range(2,int(target+1)):
        if target%i==0:
            print("%d"%i, end='')
            if target==i:
                flag=1
                break
            print('*',end='')
            target/=i
            break
