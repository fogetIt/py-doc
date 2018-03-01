# -*- coding: utf-8 -*-
# @Date:   2018-02-01 16:34:44
# @Last Modified time: 2018-03-01 16:42:40
import timeit
import dis
"""
==具有传递性，a==b, b==c会被化简为a==c
不论从遵循PEP的规范，还是执行效率，或者程序的简洁性来说，都应该使用if x
"""


def if_x():
    x = True
    if x:
        pass


def if_x_eq_true():
    x = True
    if x == True:
        pass


print(timeit.timeit(if_x, "from __main__ import if_x", number=10000000))
print(timeit.timeit(if_x_eq_true, "from __main__ import if_x_eq_true", number=10000000))

print(dis.dis(if_x))
print("#" * 20)
print(dis.dis(if_x_eq_true))
