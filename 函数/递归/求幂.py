# -*- coding: utf-8 -*-
# @Date:   2016-09-21 14:06:45
# @Last Modified time: 2016-10-19 09:31:52

dishu = int(input('底数：'))
zhishu = int(input('指数：'))


def qm(x, n):
    return x**n
print qm(dishu, zhishu)


def qiumi(x, n):
    if n <= 1:
        return x
    # if n <= 0:
    #     return 1
    else:
        return x * qiumi(x, n - 1)
print(qiumi(dishu, zhishu))
# print(9e-4)
