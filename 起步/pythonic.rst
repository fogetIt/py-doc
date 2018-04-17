python 之禅
===========
.. code-block:: python

    import this


三目运算
-------
:java/javascript: ``(expression)? (true value): (false value)``
:python:
    .. code-block:: python

        print(filter(lambda i: True if i % 2 else False, range(10)))


链式比较
-------
.. code-block:: python

    print(1 <= 3 < 10)


字符串反转
---------
.. code-block:: python

    print('mklouy'[::-1])


字符串列表连接
-------------
- 用列表实现字符串连加操作，十分高效，且不会犯错
    - python 中字符串是不可变的类型
    - 使用 **+** 连接 **2** 个字符串时会生成 **1** 个新的字符串
    - 生成新的字符串就需要重新申请内存
    - 当连续相加的字符串很多时，效率就必然低下
.. code-block:: python

    # 这样只会有一次内存的申请
    print(' '.join(["Python", "is", "good"]))
