# -*- coding: utf-8 -*-
# @Date:   2017-02-13 11:20:59
# @Last Modified time: 2018-01-16 16:37:20


def multi_fun():
    """
    返回的内层函数不要引用任何循环变量，或者后续会发生变化的变量
    """
    fs = []
    for i in range(4):
        def f(x):
            return i * x  # 返回的内层函数引用了变量i，但它并非立刻执行
        fs.append(f)
    return fs

f1, f2, f3, f4 = multi_fun()  # 等到函数都返回时，它们所引用的变量都i已经变了
print(f1(2), f2(2), f3(2), f4(2))
# def multi_fun(): return [lambda x: i * x for i in xrange(4)]
print([m(2) for m in multi_fun()])
print("-" * 20)


def multi_fun():
    """
    引用循环变量
    """
    def f(j):
        """
        创建一个函数，参数绑定循环变量当前的值
        f()函数与for循环分离，可以写在任意能调用到的地方
        """
        def g(x):
            """
            无论该循环变量后续如何更改，已绑定到函数参数的值不变
            """
            return j * x
        return g
    fs = []
    for i in range(4):
        fs.append(f(i))
    return fs
f1, f2, f3, f4 = multi_fun()
print(f1(2), f2(2), f3(2), f4(2))
