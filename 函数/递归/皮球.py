# -*- coding: utf-8 -*-
# @Date:   2016-09-20 09:18:47
# @Last Modified time: 2016-10-19 09:35:37

# 从100扔下皮球一枚，弹起50，落下再次弹起25......
# 默认当弹起高度小于1米为静止，求弹跳过程中小球弹过的路程


def dist(h0):

    def dist_(h):
        if h <= 1.0:  # 边界条件——弹起高度小于1.0，不计
            return 0
        else:
            return 2.0 * h + dist_(h / 2.0)  # 注意：整型与浮点型运算得到浮点型
    return dist_(h0 / 2) + h0
print(dist(float(input('下降时的高度：'))))
print


def xpq(num):
    if num <= 1:
        return 0
    else:
        if num / 2 <= 1:
            return num + xpq(num / 2.0)
        else:
            return num + xpq(num / 2.0) + num / 2.0
print xpq(float(input('下降时的高度：')))
