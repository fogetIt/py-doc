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
    """
    每个表利用 LinearMap 对象作为子表，建立更快的查询表
    通过 hash 函数计算索引值存放在哪个子表
    每个子表的插入、查询时间复杂度为 O(n)
    查找速度受到子表数量的限制
    当子表数量为 100 时， BetterMap 的查找速度大约是 LinearMap 的 100 倍
    """
    def __init__(self, n=100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())

    def find_map(self, k):
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self, k, v):
        map = self.find_map(k)
        map.add((k, v))

    def get(self, k):
        map = self.find_map(k)
        return map.get(k)


class HashMap(object):
    """
    初始化建立子表数量为 2 的 BetterMap
    每添加 1 条数据，统计数据量 num
    每 1 个子表放 1 对 (k, v)
    num 等于子表数时，代表子表用完了
        重新初始化建立子表数量为 2 * num 的 BetterMap
        遍历旧 BetterMap 里的数据放入新 BetterMap
        用新 BetterMap 覆盖旧 BetterMap
    新添加数据插入新 BetterMap
    如此往复

    插入操作所用时间在绝大部分情况下都是常数的，偶然出现线性
    查询操作所用时间总是常数
    基本上达到了 O(1)
    """

    def __init__(self):
        self.b_maps = BetterMap(n=2)
        self.num = 0

    def add(self, k, v):
        if self.num == len(self.b_maps.maps):
            self.resize()
        self.b_maps.add(k, v)
        self.num += 1

    def get(self, k):
        return self.b_maps.get(k)

    def resize(self):
        new_maps = BetterMap(self.num * 2)
        for map in self.b_maps.maps:
            for k, v in map.items:
                new_maps.add(k, v)
        self.b_maps = new_maps
