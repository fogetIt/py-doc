时间模块
================


时间戳
--------------

:``time.time() -> floating point number``:
:``time.mktime(tuple) -> floating point number``:

    :tuple: (year, mon, mday, hour, min, sec, wday, yday, isdst)/time.struct_time


时间字符串
------------------

:``time.ctime([seconds]) -> string``: e.g.: ``'Wed Mar 14 16:11:21 2018'``
:``time.asctime([tuple]) -> string``: e.g.: ``'Wed Mar 14 16:11:21 2018'``
:``time.strftime(format[, tuple]) -> string``:
    .. code-block:: python

        import time
        print(time.strftime("%Y-%m-%d %H-%M-%S"))  #: 2018-03-14 16-21-12


结构时间
------------------
- -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)
    - ``time.gmtime([seconds])`` (UTC)
    - ``time.localtime([seconds])``
    - ``time.struct_time(tuple)``
    - ``time.strptime(string, format)``
    :.tm_yeay: 2018


time.clock() -> floating point number
--------------------------------------

:windows:
    - 第一次调用返回进程时间
    - 之后每次调用都会返回距离第一次调用过了多长时间
:linux: 返回当前进程的 **CPU** 时间
.. code-block:: python

    import time


    def time_it(count):
        start = time.clock()
        for _ in range(count): pass
        end = time.clock()
        return (end - start)
    t1 = time_it(10000)
    t2 = time_it(3000)
    print(t1)
    print(t2)


time.sleep(seconds)
-------------------
将程序挂起指定秒


pytz
-----
- **python2**
.. code-block:: python

    import pytz
    print(pytz.country_timezones('cn'))  #: Asia/Shanghai  #: 查看时区
    pytz.timezone('Asia/Shanghai')                         #: 设置时区
