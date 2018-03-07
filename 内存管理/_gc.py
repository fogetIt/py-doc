# -*- coding: utf-8 -*-
# @Date:   2017-02-07 11:26:11
# @Last Modified time: 2018-02-02 11:09:43
import gc
from sys import getrefcount
gc.set_debug(gc.DEBUG_LEAK)
gc.disable()
print gc.get_threshold()
gc.set_threshold()
gc.get_count()
"""
"""
x = 10
print gc.collect()
del x
print gc.collect()

"""
引用环(reference cycle)
"""
# 两个对象可能相互引用，从而构成引用环
a = []
b = [a]
a.append(b)
print a, getrefcount(a)
print b, getrefcount(b)

# 一个对象自己引用自己，也能构成引用环
c = []
c.append(c)
print c, getrefcount(c)
print("-" * 20)


print gc.garbage
print gc.collect()
del a
del b

print("-" * 20)
print gc.garbage
print gc.collect()

# print gc.get_count()


class ClassA(object):
    pass


def f2():
    """
    循环引用导致内存泄露
    """
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1  # 两块内存的引用计数变成2
        del c1  # del c1后，内存1的对象的引用计数变为1
        del c2

# 执行f2()，进程占用的内存会不断增大
f2()
