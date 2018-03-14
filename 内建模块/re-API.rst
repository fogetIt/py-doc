re API
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
