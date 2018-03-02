# -*- coding: utf-8 -*-
# @Date:   2016-09-21 13:54:10
# @Last Modified time: 2018-01-16 16:01:08

# <type 'function'>
# 函数也是一个对象，可以被赋值给变量，通过变量也能调用该函数

def add(x, y, f):
    """
    高阶函数————让函数的参数能够接收别的函数
    在 Python 中函数是一级对象
    变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数
    函数式编程就是指这种高度抽象的编程范式
    """
    return f(x) + f(y)
print(add(3, -5, abs))


'''
lambda函数————单行匿名小函数————labmda *args: expression————默认return表达式的结果
可以接受任意个参数，包括可选参数
表达式（expression）只有一个
可以赋值给一个变量
'''

g = lambda x, y: x * y
print(g(3, 4))

d = lambda p: (lambda q: p * q)
print(d(2)(3))
