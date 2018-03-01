# -*- coding: utf-8 -*-
# @Date:   2016-10-15 21:23:07
# @Last Modified time: 2017-11-14 10:31:00


# 装饰器可以连用
# 被装饰函数可以接收参数


def decorator(func):
    """
    一个标准的装饰器
    根据自己的需要给主函数添加任何额外的代码
    """
    def modify(*args, **kwargs):
        """
        用 *args 和 **kwargs 接收任意的输入参数
        在此函数内调用原函数并且返回其结果
        """
        variable = kwargs.pop('variable', None)
        print variable
        x, y = func(*args, **kwargs)
        return x, y
    return modify


@decorator
def func(a, b):
    print a**2, b**2
    return a**2, b**2

func(a=4, b=5, variable="hi")
print
func(a=4, b=5)
