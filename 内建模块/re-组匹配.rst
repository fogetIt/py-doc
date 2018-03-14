普通组匹配
---------
    - 整个表达式作为 ``group(0)``
    - 如果不引入括号
        - 只有 ``group(0)``
    - 如果引入括号
        - ``()`` 内作为一个整体，匹配次数放后
        - 组编号从 1 开始，嵌套部分从 ``(`` 算起
        - 返回`()`内的匹配内容，`()` 外只作为条件
    .. code-block:: python

        import re
        S = "a1b2c3mn"
        reg = re.compile("(\w)\d")
        print(re.findall(reg, S))       #: ['a', 'b', 'c']

        print(reg.search(S).group())    #: a1
        print(reg.search(S).group(0))   #: a1  #: 获取匹配的内容 group() 默认参数是 0
        print(reg.search(S).group(1))   #: a   #: 只获取组匹配的内容
        print(reg.search(S).group(2))   #: IndexError


命名组匹配
---------
    :``(?P<name>...)``:
        .. code-block:: python

            import re
            S = "a1b2c3mn"
            reg = re.compile("(?P<nm>\w)\d")
            print(re.findall(reg, S))             #: ['a', 'b', 'c']

            print(reg.search(S).group())          #: a1           #: 获取匹配的内容
            print(reg.search(S).group(1))         #: a            #: 以索引获取组匹配的内容
            print(reg.search(S).group("nm"))      #: a            #: 以键获取组匹配的内容

            print(reg.search(S).groupdict())      #: {'nm': 'a'}  #: 获取匹配的内容字典
            print(reg.search(S).groupdict(1))     #: {'nm': 'a'}  #: 以索引获取组匹配的内容字典
            print(reg.search(S).groupdict("nm"))  #: {'nm': 'a'}  #: 以键获取组匹配的内容字典


捕获组匹配
---------
    :引用组: ``(?P=name...)``

        .. code-block:: python

            import re
            S = "a1b2c3amn"
            reg = re.compile('(?P<nm>\w)\w+(?P=nm)')
            print(re.findall(reg, S))              #: ['a']

            print(reg.search(S).group())           #: a1b2c3a      #: 获取匹配的内容
            print(reg.search(S).group(1))          #: a            #: 以索引获取组匹配的内容
            print(reg.search(S).group("nm"))       #: a            #: 以键获取组匹配的内容

            print(reg.search(S).expand("\g<0>"))   #: a1b2c3a
            print(reg.search(S).expand("\g<1>"))   #: a
            print(reg.search(S).expand("\g<nm>"))  #: a

            print(reg.search(S).groupdict())       #: {'nm': 'a'}  #: 获匹配的内容字典
            print(reg.search(S).groupdict(1))      #: {'nm': 'a'}  #: 以索引获取组匹配的内容字典
            print(reg.search(S).groupdict("nm"))   #: {'nm': 'a'}  #: 以键获取组匹配的内容字典
    :不捕获: ``(?:...)``

        - 不捕获 ``()`` 里的内容，不能使用反向引用
        - 可以提高程序执行速度


普通组与命名组混合
----------------
    先忽略命名组
