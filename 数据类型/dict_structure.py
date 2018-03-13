# -*- coding: utf-8 -*-
# @Date:   2018-03-13 15:34:23
# @Last Modified time: 2018-03-13 15:34:37


class LinearMap(object):
    """
    线性表：线性方式插入、查找元素，时间复杂度为 O(n)
    """

    def __init__(self):
        self.items = []

    def add(self, k, v):
        self.items.append((k, v))

    def get(self, k):
        for key, value in self.items:
            if k == key:
                return value
        return None


class BetterMap(object):

    def __init__(self, n=100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())

    def find_map(self): pass
    def add(self): pass
    def get(self): pass
