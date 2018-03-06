# -*- coding: utf-8 -*-
# @Date:   2017-02-07 11:26:11
# @Last Modified time: 2018-02-02 11:09:43
import gc
from sys import getrefcount
gc.set_debug(gc.DEBUG_LEAK)
"""
gc.get_threshold()————垃圾回收频率（计数阀值数目）
(700, 10, 10)
    每10次0代垃圾回收，会有1次1代垃圾回收；
    每10次1代的垃圾回收，会有1次2代垃圾回收；
"""
print gc.get_threshold()
"""
gc.set_threshold(700, 10, 5)————设置自动垃圾回收频率
gc.set_debug(flags)————设置gc的debug日志，一般设置为gc.DEBUG_LEAK
gc.garbage————存储垃圾回收后的对象的list
gc.collect([generation])
    返回此次垃圾回收的unreachable(不可达)对象个数
    显式执行垃圾回收（只对循环引用起作用）
    generation参数
        0代表只检查第一代的对象
        1代表检查一，二代的对象
        2代表检查一，二，三代的对象
        如果不传参数，执行一个full collection，也就是等于传2
gc.isenabled()————是否启动自动垃圾回收————bool，默认True
gc.get_count()————获取当前自动执行垃圾回收的计数器，返回一个长度为3的tuple

如果循环引用中，两个对象都定义了__del__方法，gc模块不会销毁这些unreachable对象，因为gc模块不知道应该先调用哪个对象的__del__方法，所以为了安全起见，gc模块会把对象放到gc.garbage中，但是不会销毁对象。
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
