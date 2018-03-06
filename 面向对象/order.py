# -*- coding: utf-8 -*-
# @Date:   2016-10-19 17:03:39
# @Last Modified time: 2018-01-15 16:21:12


class Person(object):
    attr = 'old'

    def eat(self):
        print 'eat'

    def sleep(self):
        print 'sleep'

    def other(self):
        self.hehe()

    def hehe(self):
        print 'hehe'


class Son(Person):
    attr = 'new'

    def sleep(self):
        '''
        继承时重写
        '''
        print 123

    def other(self):
        Person.other(self)

    def hehe(self):
        print self.attr

s = Son()

s.eat()
s.sleep()
print s.attr
s.other()


class Son_son(Son):
    pass

ss = Son_son()
ss.eat()


print('----------------------')


class A(object):
    attr = 123
    __attr = "hidden"

    def __method(self):
        """
        私有方法，只可以在类的内部调用
        """
        print self.__attr

    def method(self):
        """
        绑定方法，对外公开
        """
        self.__method()

a = A()
print a.attr      # 123
# print a.__attr  # 访问出错
print a._A__attr  # hidden
"""
设置的__attr与class内部的__attr不是一个变量
"""
a.__attr = 15
print a.__attr    # 15
print a._A__attr  # hidden

a.method()        # hidden
# a.__method()    # 访问出错
