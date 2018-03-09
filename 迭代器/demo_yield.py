# -*- coding: utf-8 -*-
# @Date:   2016-09-20 09:18:47
# @Last Modified time: 2017-02-20 09:50:46
#
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回
# generator函数，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行


def odd():
    """yield语句"""
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5

o = odd()
o.next()  # next()————执行到yield 1，不打印1
o.close()  # close()————退出生成器，再调next()会报错（不论生成器是否为空）
# o.next()
print

o = odd()
print o.next()  # 执行到yield 1，打印1
print


# send()————比next()开始多了一次赋值的动作（将值回送给生成器），其他运行流程相同
# next()==send(None)
print o.send(9)
print("#" * 20)


def odd():
    """yield表达式(Expression)"""
    m = yield 1
    print m  # None
    m = yield 2

o = odd()
print o.next()
print
print o.next()
o.close()
print
o = odd()
o.next()
o.send(10)  # 将10返回给m，m接收返回值
o.close()
print("#" * 20)

o = odd()
print o.__iter__    # 一个可迭代的标记
print o.gi_code     # 生成器对应的code对象
print o.gi_frame    # 生成器对应的frame对象
print o.gi_running  # 生成器函数是否在执行，yield以后、执行yield下一行代码前处于frozen状态，此时这个属性的值为0
