# coding=utf-8
"""
-------------------------------------------------
   File Name:     实例002_个税计算
   Description :
   Author :       a
   date:          2020/5/18
-------------------------------------------------

题目：
    企业发放的奖金根据利润提成
    利润(I)低于或等于10万元时，奖金可提10%；
    利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
    20万到40万之间时，高于20万元的部分，可提成5%；
    40万到60万之间时高于40万元的部分，可提成3%；
    60万到100万之间时，高于60万元的部分，可提成1.5%；
    高于100万元时，超过100万元的部分按1%提成，
    从键盘输入当月利润I，求应发放奖金总数？

    程序分析 分区间计算即可
    profit - 利润
    bonus - 奖金
"""


profit = int(input("Please input the profit(利润): "))
bonus = 0.0
I = profit
#
# if profit <= 10:
#     bonus = profit * 0.1
# elif profit > 10 and profit <= 20:
#     bonus = 10 * 0.1 + (profit - 10) * 0.075
# elif profit > 20 and profit <= 40:
#     bonus = 10 * 0.1 + 10 * 0.075 + (profit - 20) * 0.05
# elif profit > 40 and profit <= 60:
#     bonus = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (profit - 40) * 0.03
# elif profit > 60 and profit <= 100:
#     bonus = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (profit - 60) * 0.015
# elif profit > 100:
#     bonus = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (profit - 100) * 0.01
#
# print("%.2f 的提成为%.2f." % (profit, bonus))

# while (profit > 0):
# #     if profit > 100:
# #         profit = profit - 100
# #         bonus += profit * 0.01
# #     if profit > 60 and profit <= 100:
# #         profit = profit - 60
# #         bonus += profit * 0.015
# #     if profit > 40 and profit <= 60:
# #         profit = profit - 40
# #         bonus += profit * 0.03
# #     if profit > 20 and profit <= 40:
# #         profit = profit - 20
# #         bonus += profit * 0.05
# #     if profit > 10 and profit <= 20:
# #         profit = profit - 10
# #         bonus += profit * 0.075
# #     if profit <= 10:
# #         bonus += profit * 0.01
# #         break
# #
# # print("%.2f 的提成为%.2f." % (profit, bonus))

thresholds = [100000, 100000, 200000, 200000, 400000]
rates = [0.1, 0.075, 0.05, 0.015, 0.01]

for i in range(len(thresholds)):
    if profit < thresholds[i]:
        bonus += profit * rates[i]
        profit=0
        break
    else:
        bonus += thresholds[i] * rates[i]
        profit -= thresholds[i]
bonus += profit * rates[-1]
print("%.2f 的提成为%.2f." % (I, bonus))


