# -*- coding: utf-8 -*-
# @Date:   2016-10-17 09:08:45
# @Last Modified time: 2017-03-01 18:41:32
import traceback
import traceback_


def demo():
    print 1 / 0

# 用try..except捕获异常，然后traceback.print_exc()打印


try:
    # demo()
    traceback_.demo()
except Exception as e:
    # print 'Exception', e    # 直接打印异常
    traceback.print_exc()     # 打印异常的详细信息==print traceback.format_exc()
    # traceback.format_exc()  # 返回异常的详细信息

print 123
print 456
