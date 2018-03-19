##### install
- Windows 下不保证正常安装和运行
- pip install greenlet
- pip install gevent
- [下载](https://pypi.python.org/pypi/gevent#downloads)


##### 队列
```python
# coding: utf-8
from gevent.queue import Queue, Empty, LifoQueue, PriorityQueue, JoinableQueue
"""
Greenlet 之间的线程内同步的队列
无线程同步开销
无法跨线程间操作
"""
```

##### 协程池
```python
# coding: utf-8
from gevent import monkey
from gevent.pool import Pool, Group
monkey.patch_all()

g = Group()          # 管理一组 greenlet
g = Pool(size=None)  # 继承 Group() ，可以限制并发量
# 持续追加
g.add(greenlet)
g.apply_async(func, args=None, kwds=None, callback=None)
g.map(func, iterable)
# 创建一个greenlet，并将其switch()加入hub主循环回调
g.spawn(*args, ***kwargs)
# 批量等待
g.join()
```

##### 文档
[中文官网](http://xlambda.com/gevent-tutorial/)
[stackflow](https://stackoverflow.com/questions/tagged/gevent)
http://www.it165.net/admin/html/201308/1682.html
http://rfyiamcool.blog.51cto.com/1030776/1276364/
https://my.oschina.net/visualgui823/blog/36987
http://blog.csdn.net/handsomekang/article/details/39826729
http://brieflyx.me/2015/python-module/python-lib-multiprocessing/

##### gevent.hub.LoopExit
- 原因
    + Queue().get() 默认是堵塞的（线程一直堵塞到有任务返回）
    + gevent hub，一个特殊的 greenlet ，相当于主线程（调度器）
    + gevent hub 不会让某个 greenlet 独占线程的 cpu 执行资源，肯定会把该任务切换到 hub 里
    + 当所有 greenlet 都在做 waiter 操作（网络I/O、queue），会造成 gevent 切换 hub 失败
- 解决方法
    + 避免使用 waiter 事件
        ```python
        Queue().get_nowait()
        ```
    + 有一个任务一直在跑着
    + 使用 gevent.queue.JoinableQueue
        * 继承 Queue
        * 构造一个“未完成”的计数器
        * 每次触发 put() 的时候需要加一个计数
        * 每次触发 task_done() 的时候才会减一，重置 self._cond.set()
