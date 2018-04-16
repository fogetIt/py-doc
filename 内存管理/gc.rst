gc 模块
=======
- **python** 内存管理模块
- 负责跟踪和回收垃圾
- 管理大多数对象的 **生命周期**


API
---

gc.disable() -> None
""""""""""""""""""""
暂停自动垃圾回收


gc.isenabled() -> bool
""""""""""""""""""""""
是否启动了自动垃圾回收，默认 **True**


gc.collect([generation]) -> n
"""""""""""""""""""""""""""""
- 显式地执行一次完整的 `垃圾回收（标记-清除、分代回收） <垃圾回收.rst>`_
    - **gc** 模块会根据 **threshold** 阀值自动进行分代回收
    - 如果程序中有 **占用内存较大的对象** ，可以显式地执行垃圾回收
    :``generation``: 指定执行回收的代数，默认是 **2**

        :``0``: 只检查第 **1** 代的对象
        :``1``: 检查 **1** 、 **2** 代的对象
        :``2``: 检查 **1** 、 **2** 、 **3** 代的对象
- 返回回收的 ``unreachable`` 对象数


gc.get_count() -> (count0, count1, count2)
""""""""""""""""""""""""""""""""""""""""""
- 当前自动执行垃圾回收的计数器

:``object allocation``:                           **python** 运行时分配对象的次数
:``object deallocation``:                         **python** 运行时取消分配对象的次数
:``object allocation`` - ``object deallocation``: 没有释放的对象个数


gc.get_threshold() -> (threshold0, threshold1, threshold2)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
垃圾回收频率的计数阈值


gc.set_threshold(threshold0, threshold1=None, threshold2=None) -> None
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
- 设置垃圾回收频率的计数阈值

:``threshold0``: 执行 **1** 次 **0** 代回收的需要积累多少个没有释放的对象
:``threshold1``: 执行 **1** 次 **1** 代回收需要经过几次 **0** 代回收
:``threshold2``: 执行 **1** 次 **2** 代回收需要经过几次 **1** 代回收


gc.garbage
"""""""""""
存储垃圾回收后的对象的 ``list``


gc.set_debug(flags) -> None
""""""""""""""""""""""""""""
- 设置垃圾回收的调试标记. 调试信息会被写入 ``std.err``

    :gc.DEBUG_STATS:
    :gc.DEBUG_LEAK:         打印内存泄漏的对象
    :gc.DEBUG_COLLETABLE:   打印可以被垃圾回收器回收的对象
    :gc.DEBUG_UNCOLLETABLE: 打印无法被垃圾回收器回收的对象（定义了 ``__del__`` 的对象）
    :gc.DEBUG_SAVEALL:      可回收对象不会被真正销毁（ ``free`` ），而是放到 ``gc.garbage``

        - 利于在线上查找问题


gc.get_objects() -> [...]
""""""""""""""""""""""""""
返回所有被垃圾回收器管理的对象


gc.get_referents(*obj) -> list
"""""""""""""""""""""""""""""""
返回 obj 直接指向的对象


gc.get_referrers(*obj) -> list
""""""""""""""""""""""""""""""
返回所有直接指向obj的对象
