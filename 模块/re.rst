正则
====
- 在文本中查找匹配的字符串

=============  ======
匹配顺序
``^``            开头
``$``            结尾
``\A``           仅开头
``\Z``           仅结尾
匹配数量
``*``            0~∞
``?``            0~1
``+``            1~∞
``{3}``          匹配指定次数
``{3,5}``        匹配指定范围次数
匹配内容
``.``            除换行外所有内容
``\w``           数字、字母、下划线
``\W``           非数字、非字母、非下划线
``\b``           非 ``\w`` 、非 ``\W`` ，如 ``\b!``
``\d``           数字
``\D``           非数字
``\s``           所有的空格：``\t, \n``
``\S``           所有的非空格
``[az]``         当中的任意元素
``[a-z]``        匹配一个指定范围的 **assci** 码
``[^xxx]``       取非
``[xxx|xxx]``    或匹配，匹配两边任意一边
=============  ======


匹配中文
---------------------

:``u"[\u4e00-\u9fa5]"``:
    .. code-block:: python

        S = u"中国 China"
        o = re.findall(u"[\u4e00-\u9fa5]", S)
        for i in o: print(i, end=" ")  # 中 国


转义符
--------------
.. code-block:: python

    import re

    # 文本字符 \，需要用 \ 转义
    s = "qwert, \12345"
    S = "qwert, \\12345"
    print(s)  #: qwert, S45
    print(S)  #: qwert, \12345

    # 匹配文本字符 \ ，需要 \\\\
    print(re.findall("\\\\", S))  #: ['\\']

    # python 原生字符串
    print(r"qwert, \12345")      #: qwert, \12345
    print(re.findall(r"\\", S))  #: ['\\']


贪婪/非贪婪
--------------------

:贪婪模式:  总是尝试匹配尽可能多的字符
:非贪婪模式: 总是尝试匹配尽可能少的字符
- python 正则表达式里数量词默认是贪婪的（其它语言里可能不是）
.. code-block:: python

    import re
    S = "abbacc"
    """
    非贪婪操作符"?"，要求正则匹配的越少越好
    可以用在 "*" "+" "?" 后面
    """
    print(re.findall('ab*', S), re.findall('ab*?', S))  #: ['abb', 'a'] ['a', 'a']
    print(re.findall('ab+', S), re.findall('ab+?', S))  #: ['abb'] ['ab']
    print(re.findall('ab?', S), re.findall('ab??', S))  #: ['ab', 'a'] ['a', 'a']

----------

组匹配
===========

普通组匹配
-----------------

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

-------------------

API
======


re.compile(pattern, flags=0)
----------------------------
    :``.match(string, flags=0)``: 调用 ``re.match``
    :``.search(string, flags=0)``: 调用 ``re.search``
    :``.findall(string, flags=0)``: 调用 ``re.findall``
    - ``re.compile(...).match(...) == re.match(re.compile(...)...) == re.match(...)`` ，其它函数与此类似


生成匹配对象
-----------
    :``re.match(pattern, string, flags=0) -> _sre.SRE_Match object/None``: 在开头匹配 1 次
    :``re.search(pattern, string, flags=0) -> _sre.SRE_Match object/None``: 匹配 1 次


获取匹配对象信息
--------------
    :``.group(num)``:   匹配到的组（0，代表所有）
    :``.start(group)``: 某一组匹配的起始位
    :``.end(group)``:   某一组匹配的结束位
    :``.span(group)``:  某一组匹配的 (起始, 结束)


直接获取匹配结果
--------------
    :``re.findall(pattern, string, flags=0) -> list of str``: 匹配多次


re.split(pattern, string, maxsplit=0, flags=0) -> list
-------------------------------------------------------
    - ``str.split([sep [,maxsplit]]) -> list`` 的加强版
    - 按照能够匹配的子串将字符串分割，返回列表
    :maxsplit: 指定最大分割次数，默认全部分割


re.finditer(pattern, string, flags=0) -> iteator
-------------------------------------------------
    - ``str.find(sub[, start[, end]]) -> int`` 的加强版
    - 搜索字符串，返回一个包含顺序匹配结果（Match对象）的迭代器
    .. code-block:: python

        result = match.next().group()


re.sub(pattern, repl, string, count=0, flags=0) -> None
--------------------------------------------------------
    - ``str.replace(old, new[, count]) -> string`` 的加强版
    - 使用 **repl** 替换 **string** 中每一个匹配的子串后返回替换后的字符串
        - 当 **repl** 是一个字符串时
            - 可以使用 ``\id`` 或 ``\g<id>, \g<name>`` 引用分组，但不能使用编号 0
        + 当 **repl** 是一个方法时
            * 这个方法应当只接受一个参数(Match对象)
            * 并返回一个字符串用于替换(返回的字符串中不能再引用分组)
    :count: 用于指定最大替换次数，默认全部替换


flags
------
    :re.M: 多行模式，改变'^'和'$'的行为（忽略开始和结尾的换行符）
    :re.S: 点任意匹配模式，改变'.'的行为（匹配出 ``\n`` ）
    :re.L: 使预定字符类 ``\w \W \b \B \s \S`` 取决于当前区域设定
    :re.U: 使预定字符类 ``\w \W \b \B \s \S \d \D`` 取决于 unicode 定义的字符属性
    :re.X: 详细模式，这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释
    :re.I: 忽略大小写匹配
