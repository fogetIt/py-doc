# -*- coding: utf-8 -*-
# @Date:   2017-02-07 11:26:11
# @Last Modified time: 2018-02-02 11:09:43
import gc
from sys import getrefcount
gc.set_debug(gc.DEBUG_LEAK)
# gc.disable()
# print gc.get_threshold()
# print(gc.set_threshold())
# gc.set_threshold()
# gc.get_count()
# """
# """
# x = 10
# print gc.collect()
# del x
# print gc.collect()
#
# """
# 引用环(reference cycle)
# """
# # 两个对象可能相互引用，从而构成引用环
# a = []
# b = [a]
# a.append(b)
# print a, getrefcount(a)
# print b, getrefcount(b)
#
# # 一个对象自己引用自己，也能构成引用环
# c = []
# c.append(c)
# print c, getrefcount(c)
# print("-" * 20)
#
#
# print gc.garbage
# print gc.collect()
# del a
# del b
#
# print("-" * 20)
# print gc.garbage
# print gc.collect()
#
# # print gc.get_count()



