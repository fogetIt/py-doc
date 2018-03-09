# -*- coding: utf-8 -*-
# @Date:   2016-10-14 13:42:51
# @Last Modified time: 2017-02-17 15:17:53
from collections import Iterable
"""
collections.Iterable————可迭代对象基类
isinstance(obj, Iterable)————判断对象是否可迭代
"""
print isinstance('abc', Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance({'a': 1}, Iterable)
print isinstance(123, Iterable)
print

"""
iterator
"""
it = iter('collection')
print it
print isinstance(it, Iterable)
print it.next()
print it.next()
print it.next()
print

"""
xrange()————生成一个xrange对象————类似生成器，执行效率高于range()
xrange没有next()函数
xrange可以反复迭代
xrange可以使用下标取值
在python3中xrange()生成的对象，只能以next()方式迭代取值
"""
xr = xrange(10)
print xr, type(xr)
print isinstance(xr, Iterable)
# print xr.next()
print xr[1]
print xr[1]
print[i for i in xr if not i % 5]


"""
xrange不支持切片迭代
for i in xrange(10)[::]:
    print i,
"""
