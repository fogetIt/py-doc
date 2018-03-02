string 模块
===========
====================  ========
attrs                   return
====================  ========
``letters``             ``[a-z],[A-Z]``
``ascii_letters``       ``[a-z],[A-Z]``
``lowercase``           ``[a-z]``
``ascii_lowercase``     ``[a-z]``
``uppercase``           ``[A-Z]``
``ascii_uppercase``     ``[A-Z]``
``digits``              ``[0-9]``
``hexdigits``           ``[0-9],[a-f],[A-F]``
``octdigits``           ``[0-7]``
``punctuation``         ``!"#$%&'()*+,-./:;<=>?@[\]^_`{&#124;}~``
``printable``           上述所有
``whitespace``          ``\s,\n,\t``
====================  ========


methods
-------
    .. code-block:: python

        import string
        """
        其它方法类似
        """
        string.capitalize(s) == s.capitalize()


自定义对称加密
------------
    .. code-block:: python

        from string import maketrans
        # maketrans(frm, to) -> string
        table = maketrans(frm, to)  # 指定翻译方式
        S.translate(table)


自定义模板转义
------------
    .. code-block:: python

        from string import Template
        s = Template('$who likes $what')
        print(s.substitute(who='monkey', what='banana'))
