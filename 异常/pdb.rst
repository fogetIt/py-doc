pdb 命令
========
    - ``sublime repl_python_pdb`` 用法
    =========================================  =======
    command                                      todo
    =========================================  =======
    ``h(elp)[command]``                          打印当前版本 **pdb** 可用的命令
    ``l(ist) [first [,last]]``                   列出代码块（默认第一行起）
     -
    ``b(reak)``                                  显示所有断点信息
    ``b(reak) [file:]linenum/function``          建立断点
     -
    ``condition bpnum [condition]``              设置条件断点
     -
    ``cl(ear)``                                  去除所有断点
    ``cl(ear) [file:]linenum/bpnum bpnum...``    去除断点
     -
    ``disable bpnum``                            禁用断点
    ``enable bpnum``                             激活断点
     -
    ``ignore``                                   设定断点的忽略次数
    ``n(ext)``                                   下一行，不进入函数
    ``s(tep)``                                   下一行，进入函数
    ``c(ont(inue))``                             继续
     -                                           正常运行，直到断点
    ``j(ump)``                                   跳转到指定的行数
     -
    ``a(rgs)``                                   打印所在函数参数
    ``p [param]``                                打印 **expression**
    ``pp [param]``                               使用 **pprint** 打印 **expression**
    ``! statement``                              直接改变某个变量
     -
    ``w``                                        列出目前 **callstack** 中的所在层
    ``d(own)``                                   在 **callstack** 中往下移一层
    ``u(p)``                                     在 **callstack** 中往上移一层
    ``r(eturn)``                                 执行到 **return**
    ``q(uit)/exit``                              退出
    =========================================  =======
