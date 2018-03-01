# -*- coding: utf-8 -*-
# @Date:   2017-01-20 09:56:32
# @Last Modified time: 2018-03-01 16:47:45
import timeit
import dis


def while_1():
    i = 0
    while 1:
        i += 1
        if i == 10000000:
            break


def while_true():
    i = 0
    while True:
        i += 1
        if i == 10000000:
            break
"""
wihle 1的执行时间比while True短
wihle 1被程序进行了优化，不会进行检查
"""
print(timeit.timeit(while_1, "from __main__ import while_1", number=3))
print(timeit.timeit(while_true, "from __main__ import while_true", number=3))

"""
查看 while_1 和 while_true 的字节码
while True 的字节码中多了对 True 值的检查
"""

print(dis.dis(while_1))
print("#" * 20)
print(dis.dis(while_true))
