# -*- coding: utf-8 -*-
# @Date:   2017-03-01 18:29:02
# @Last Modified time: 2017-03-01 18:29:10
import sys
"""
os._exit()调用C语言的_exit()，直接退出Python程序，其后的代码都不会执行，用于在线程中退出；
sys.exit()引发一个SystemExit异常（Exception捕捉不到），用于在主线程中退出；

若没有捕获这个异常，Python解释器会直接退出；
捕获这个异常可以做一些额外的清理工作
exit(0)————正常退出，用在循环语句调用的非循环函数里
exit(1~127)————不正常，抛出异常事件供捕获
"""


def demo(a=0):
    try:
        if a:
            sys.exit(0)
        else:
            sys.exit(10)
    except SystemExit as e:
        print e
    finally:
        print 'finally'


demo(10)
print
demo()
