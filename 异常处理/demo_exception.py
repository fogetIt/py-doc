# -*- coding: utf-8 -*-
# @Date:   2016-07-12 13:06:08
# @Last Modified time: 2017-11-21 11:05:41
#
"""
except [exception1[,exception2...] as obj]
python3 不再支持 except Exception, e，必须使用 as
捕获异常类型（exception1[,exception2...]）的详细原因，并放在对象（obj）中
"""
import os
filepath = os.path.abspath('.')
print filepath


"""
异常处理语句嵌套
"""
try:
    f = open(filepath, 'r')
    """
    外层try子句代码引发异常
    程序直接跳转到外层try对应的except子句
    内部的try子句不会被执行
    """
    try:
        print 'ok'
    except:
        print 'no'
except ValueError as e:
    print 'ValueError:', e
except IOError, e:
    print 'IOError', e
    try:
        filename = os.path.join(filepath, 'demo_exception.py')
        f = open(filename, 'r')
        f.close()
        print 'ok'
    except Exception, e:
        print 'inner:', e
except Exception, e:
    """
    多个并列的except语句，子类异常写在前面，父类写在后面
    """
    print 'outer:', e
print
