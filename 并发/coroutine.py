# -*- coding: utf-8 -*-
# @Date:   2018-03-19 09:42:26
# @Last Modified time: 2018-03-19 10:14:47
import time


def w1():
    r = ""
    while True:
        print(r)
        n = yield r          #: step: 2 4 6
        if not n:
            return
        print("worker1", n)
        time.sleep(1)
        r = "ok"


def w2(w):
    w.__next__()             #: step: 1
    i = 0
    while i < 3:
        i += 1
        print("worker2", i)
        r = w.send(i)        #: step: 3 5 7
        print("worker1", r)
    w.close()


w = w1()
w2(w)
print("*" * 20)
# --------------------------------------------------------
import threading
import asyncio


@asyncio.coroutine
def g1():
    print("python3.4", threading.get_ident(), "start")
    yield from asyncio.sleep(4)
    print("python3.4", threading.get_ident(), "end")


async def g2():
    print("python3.5", threading.get_ident(), "start")
    await asyncio.sleep(4)
    print("python3.5", threading.get_ident(), "end")

# @asyncio.coroutine/async  #: 把一个 generator 标记为 coroutine 类型
# yield from/await          #: 等待另一个 generator

"""
asyncio
    实现了 TCP、UDP、SSL 等协议
    可以单线程并发 IO 操作
aiohttp
    基于 asyncio 实现的 HTTP 框架
"""
loop = asyncio.get_event_loop()
tasks = [g1(), g2()]
print(asyncio.iscoroutine(g1()))  #: True
print(asyncio.iscoroutine(g2()))  #: True


print("*" * 20)
#: 把协程对象包装（wrap）成了 future
future = asyncio.ensure_future(g2())
#: 往 future 添加回调函数，获取协程结束通知
future.add_done_callback(lambda arg: print(arg))
#: 阻塞调用，直到协程运行结束
loop.run_until_complete(future)
print("*" * 20)


# loop.run_until_complete(asyncio.wait(tasks))
loop.run_until_complete(asyncio.gather(*tasks))
print("success")
loop.close()
