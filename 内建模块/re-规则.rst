正则
====
    - 用于在文本中查找匹配的字符串
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
-------
    :``u"[\u4e00-\u9fa5]"``:
        .. code-block:: python

            S = u"中国 China"
            o = re.findall(u"[\u4e00-\u9fa5]", S)
            for i in o: print(i, end=" ")  # 中 国


转义符
------
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
----------
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
