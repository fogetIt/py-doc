# -*- coding: utf-8 -*-
# @Date:   2016-10-17 09:08:45
# @Last Modified time: 2017-02-13 17:26:28
#
'''
当程序出现错误，python会自动引发异常
raise————显式地引发异常
'''
s = None
try:
    if s is None:
        print 's 是空对象'
        raise NameError  # 一旦执行了raise语句，raise后面的语句将不能执行
        print '出错了'
    print len(s)
except NameError:
    print '对象错误'
else:
    print '没有出错'
finally:  # finally子句关闭因异常而不能释放的系统资源
    print '释放资源'
