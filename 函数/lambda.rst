labmda *args: expression
========================
    - 单行匿名小函数
    :*args:      可以接受任意个参数，包括可选参数
    :expression: 表达式，只有 **1** 个
    - 可以赋值给一个变量，返回表达式的结果
    .. code-block:: python

        f = lambda a, b=1: a + b
        print(f)    # in PY2 <type 'function'>, in PY3 <class 'function'>
        print(f(2)) # 3


嵌套 lambda
-----------
    .. code-block:: python

        f = lambda a: (lambda b: a * b)
        print(f(2)(3)) # 6


lambda 函数直接修改外部的不可变对象
-------------------------------
    .. code-block:: python

        i = 0
        a = lambda : lambda : i + 1
        print(a()()) #: 1
        print(i)     #: 0