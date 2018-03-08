# -*- coding: utf-8 -*-
# @Date:   2016-07-12 13:06:08
# @Last Modified time: 2017-11-21 11:05:41


"""
异常处理语句嵌套
    外层 try 子句代码引发异常，程序直接跳转到对应的外层 except 子句
    内部的 try 子句不会被执行
多个并列的 except 语句
    子类异常写在前面，父类写在后面，否则捕获不到子类异常
"""
try:
    print( 2 / 0)
    try: print('ok')
    except: print('no')
except ZeroDivisionError as e:
    print('ZeroDivisionError', e)
    try: print(2 / 1)
    except Exception as e: print('inner:', e)
except Exception as e:
    print('outer:', e)


try:
    print( 2 / 0)
    try: print('ok')
    except: print('no')
except ZeroDivisionError as e:
    print('ZeroDivisionError', e)
    try: print(2 / 1)
    except Exception as e: print('inner:', e)
except Exception as e:
    print('outer:', e)
