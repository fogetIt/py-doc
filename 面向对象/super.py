# -*- coding: utf-8 -*-
# @Date:   2016-11-22 10:17:50
# @Last Modified time: 2018-03-06 16:28:34


class A(object):  # A must be new-style class

    def __init__(self):
        print("A",)
        print("A",)


class B(object):

    def __init__(self):
        print("B",)
        print("B",)


class C(A):

    def __init__(self):
        print("C",)
        A.__init__(self)
        print("C",)


class D(A):

    def __init__(self):
        print("D",)
        A.__init__(self)
        print("D",)


class E(B, C):

    def __init__(self):
        print("E",)
        B.__init__(self)
        C.__init__(self)
        print("E",)


class F(E, D):

    def __init__(self):
        print("F",)
        E.__init__(self)
        D.__init__(self)
        print("F",)
f = F()
print()
print(F.__mro__)
print('--------------------------')


class A(object):

    def __init__(self):
        print("A",)
        super(A, self).__init__()
        print("A",)


class B(object):

    def __init__(self):
        print("B",)
        super(B, self).__init__()
        print("B",)


class C(A):

    def __init__(self):
        print("C",)
        super(C, self).__init__()
        print("C",)


class D(A):

    def __init__(self):
        print("D",)
        super(D, self).__init__()
        print("D",)


class E(B, C):

    def __init__(self):
        print("E",)
        super(E, self).__init__()
        print("E",)


class F(E, D):

    def __init__(self):
        print("F",)
        super(F, self).__init__()
        print("F",)
f = F()
print()
print(F.__mro__)
