##### `repl_python_pdb`插件用法

|命令                                    |含义                     |
|:--------------------------------------|:-----------------------|
|h(elp)[命令名称]                        |打印当前版本Pdb可用的命令  |
|l(ist) [first [,last]]                 |列出代码块（默认第一行起）   |
|                                       |                        |
|b(reak) [[file:]linenum/function]      |显示所有断点信息/建立断点   |
|condition bpnum [condition]            |设置条件断点              |
|cl(ear) [[file:]linenum/bpnum bpnum...]|去除（默认所有）断点        |
|disable/enable bpnum                   |禁用/激活断点             |
|ignore                                 |设定断点的忽略次数         |
|                                       |                        |
|n(ext)                                 |下一行，不进入函数         |
|s(tep)                                 |下一行，进入函数           |
|c(ont(inue))                           |（继续）正常运行，直到断点    |
|j(ump)                                 |跳转到指定的行数          |
|                                       |                        |
|a(rgs)                                 |打印所在函数参数          |
|p [param]                              |打印expression           |
|pp [param]                             |和p类似,但是使用pprint    |
|! statement                            |直接改变某个变量          |
|                                       |                        |
|w                                      |列出目前callstack中的所在层|
|d(own)                                 |在callstack中往下移一层   |
|u                                      |在callstack中往上移一层   |
|                                       |                        |
|r(eturn)                               |执行到return             |
|q(uit)/exit                            |退出                     |
