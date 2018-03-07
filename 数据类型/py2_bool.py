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


def while_t():
    i = 0
    while True:
        i += 1
        if i == 10000000:
            break
"""
在 python2 中
每次循环时都需要对 True/False 值进行额外耗时的检查
wihle 1 被程序进行了优化，不会进行检查，因此执行时间比 while True 短
"""
print(timeit.timeit(while_1, "from __main__ import while_1", number=3))
print(timeit.timeit(while_t, "from __main__ import while_t", number=3))


"""
查看 while_1 和 while_t 的字节码
在 python2 中
    while True 的字节码中多了对 True 值的检查
在 python3 中
    没有区别
"""

print(dis.dis(while_1))
print("*" * 20)
print(dis.dis(while_t))
