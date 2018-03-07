# -*- coding: utf-8 -*-
# @Date:   2017-02-06 17:27:59
# @Last Modified time: 2018-03-07 11:35:27
"""
引用计数(reference count)：指向每个对象的引用总数
sys.getrefcount(object) -> Integer
    查看对象的引用计数
    创建了一个临时引用，结果比期望值多 1
"""
from sys import getrefcount


"""
对象的引用计数 +1
"""
a = [1, 2, 3]
print(getrefcount(a))  #: 2(0+1+1)    #: 对象被创建
b = a
print(getrefcount(a))  #: 3(1+1)      #: 对象被引用
l = [a, a, a]
print(getrefcount(a))  #: 6(3+1+1+1)  #: 对象作为一个元素，存储在容器中
def f(): x = a; return getrefcount(a)
print(f())             #: 7(6+1)      #: 本地引用
f = lambda a: getrefcount(a)
print(f(a))            #: 9(6+1+1+1)  #: 本地引用 +1+1+1
print("*" * 30)
"""
对象的引用计数 -1
"""
print(getrefcount(a))  #: 6(9-1-1-1)  #: 本地引用结束
del b
print(getrefcount(a))  #: 5(6-1)      #: del 对象
del l[0]
print(getrefcount(a))  #: 4(5-1)      #: 对象被从一个窗口对象移除
l[0] = 0
print(getrefcount(a))  #: 3(4-1)      #: 对象的引用被重新赋值
del l
print(getrefcount(a))  #: 2(3-1)      #: del 窗口对象
print("*" * 30)
"""
引用计数归 0，置为 1
"""
a = [0]
print(getrefcount(a))  #: 2(0+1+1)    #: 重新赋值
