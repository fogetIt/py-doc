# -*- coding: utf-8 -*-
# @Date:   2017-02-06 10:38:22
# @Last Modified time: 2018-03-01 11:34:01


class C(object):
    """docstring for C"""

    def __init__(self, arg):
        self.arg = arg

    def t1(self):
        print(self.arg)


c = C('arg')
# python2.x
print(C.t1.im_func)  # <function t1 at 0x7fcaf8a3c230>
print(c.t1.im_func)  # <function t1 at 0x7fcaf8a3c230>
print(C.t1.im_self)  # None
print(c.t1.im_self)  # <__main__.C object at 0x7fcaf8a35c90>
print(C.t1.im_class) # <class '__main__.C'>
print(c.t1.im_class) # <class '__main__.C'>

# python3.x
print(c.t1.__func__)           # <function t1 at 0x7fcaf8a3c230>
print(c.t1.__self__)           # <__main__.C object at 0x7fcaf8a35c90>
print(c.t1.__self__.__class__) # <class '__main__.C'>
