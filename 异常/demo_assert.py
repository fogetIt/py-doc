# -*- coding: utf-8 -*-
# @Date:   2016-08-12 11:20:29
# @Last Modified time: 2018-02-27 09:48:06
#
"""
assert 表达式[, 消息]————声明某个条件是真的，失败的时候会引发AssertionError
（raise AssertionError-if not True）
断言是一种防御型编程————不是防御现在的错误，而是防止在代码修改后引发的错误

比较肯定代码但是不是绝对肯定时，通过额外的运行时检查，尽早地被捕捉到任何错误
检查程序依赖的不变量，尽早发现bug
"""
L = ['item']
try:
    assert len(L) >= 10, '列表参数小于10'
    print L.pop()
except AssertionError as e:
    print e


import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEquals(10, 101 / 10.0, 10)

"""
assertEquals([String message],expected,actual[,tolerance])
"""
unittest.main()
