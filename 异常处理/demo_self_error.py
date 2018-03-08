# -*- coding: utf-8 -*-
# @Date:   2016-08-12 16:43:25
# @Last Modified time: 2018-01-17 09:45:36
#
'''
自定义异常————用于描述python中没有涉及的异常情况
命名规范————以"Error"结尾
必须继承Exception类
（只能）使用raise语句引发
'''


class SelfError(Exception):

    def __init__(self, x, y):
        Exception.__init__(self, x, y)  # 调用基类的__init__进行初始化
        self.x = x
        self.y = y

print SelfError(2, 3)
print
x = 3
y = 2
try:
    if x % y > 0:  # 大于0，抛出异常
        print x / y
        raise SelfError(x, y)
except SelfError, e:  # div表示SelfError的实例对象
    print e, '%.2f' % (e.x / e.y)
