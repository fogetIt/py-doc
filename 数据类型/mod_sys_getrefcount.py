# -*- coding: utf-8 -*-
# @Date:   2017-02-06 17:27:59
# @Last Modified time: 2017-02-07 11:39:00
#
# 引用计数(reference count)————指向每个对象的引用总数
#
from sys import getrefcount
print getrefcount([1, 2, 3])
a = [1, 2, 3]         # 对象被创建，对象的引用计数+1————1
print getrefcount(a)  # getrefcount(var)，var创建了一个临时引用，结果比期望值+1————2
b = a
print getrefcount(a)  # 对象被引用，对象的引用计数+1————3
del b
print getrefcount(a)  # del对象，对象的引用计数-1————2
b = [a, a]
print getrefcount(a)  # 对象被引用，对象的引用计数+1+1————4
del b
print getrefcount(a)  # del窗口对象，对象的引用计数-1-1————2
b = [a, a]
print getrefcount(a)  # 对象被引用，对象的引用计数+1+1————4
del b[0]
print getrefcount(a)  # 对象被从一个窗口对象移除，对象的引用计数-1————3
print


def x():
    x = a
    print getrefcount(a)  # 本地引用，对象的引用计数+1————4
x1 = x()
print getrefcount(a)      # 本地引用结束，对象的引用计数-1————3
a = ['10123']
print getrefcount(a)      # 重新赋值，引用计数归零，置为1————2


# 变量名本身也是对象（没有类型），也占有内存地址（内存引用的标示），容器id指向变量名
#
# Python容器对象(container)，可以包含多个对象，指向各个元素对象的引用
# objgraph包————绘制python容器的引用关系————依赖xdot
# pip install xdot
# pip install objgraph
import objgraph

x = [1, 2, 3]
y = [x, dict(key1=x)]
z = [y, (x, y)]

# objgraph.show_refs([z], filename='ref_topo.png')
