# -*- coding: utf-8 -*-
# @Date:   2016-09-21 14:05:46
# @Last Modified time: 2016-10-19 09:36:15
num = int(input('几的阶乘：'))

# while


def jie_cheng(num):
    final = 1
    while num > 0:
        final *= num
        num -= 1
    return final
print jie_cheng(num)

# for


def jiecheng():
    final = 1
    for i in range(1, num + 1):
        final *= i
    return final
print jiecheng()

# 递归


def dg_jc(num):
    if num <= 1:
        return 1
    return num * dg_jc(num - 1)
print dg_jc(num)
# 5 * dg_jc(4)
# 5 * 4 * dg_jc(3)
# 5 * 4 * 3 * dg_jc(2)
# 5 * 4 * 3 * 2 * dg_jc(1)
# 5 * 4 * 3 * 2 * 1
