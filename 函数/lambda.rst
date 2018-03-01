

lambda 函数直接修改外部的不可变对象
-------------------------------
    .. code-block:: python

        i = 0
        a = lambda : lambda : i + 1
        print(a()()) #: 1
        print(i)     #: 0