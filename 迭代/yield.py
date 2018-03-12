# -*- coding: utf-8 -*-
# @Date:   2016-09-20 09:18:47
# @Last Modified time: 2018-03-09 18:37:34


def odd():
    print('step 1', end="---")
    yield 1
    print('step 2', end="---")
    yield 3
    print('step 3', end="---")
    yield 5


o = odd()
print(o.__iter__())   #: <generator ...>
print(o.gi_code)      #: <code ...>        #: 生成器对应的 code 对象
print(o.gi_frame)     #: <frame ...>/None  #: 生成器对应的 frame 对象
print(o.gi_running)   #: False             #: 生成器函数是否在执行

print(o.__next__())   #: step 1---1        #: 拥有 __next__()
for i in o: print(i)  #: step 2---3
                      #: step 3---5
for i in o: print(i)  #:                   #: 只能迭代一次
print("*" * 20)


o = odd()
o.close()            #: 退出生成器，不论生成器是否为空
# print(o.__next__())  #: StopIteration
print("*" * 20)



def count(n):
    x = 0
    while x < n:
        value = yield x  #: 接收外部传参
        if value is not None:
            print(value, end=" ")
        x += 1
gen = count(5)
print(gen.__next__())     #: 0
print(gen.send('Hello'))  #: Hello 1  #: 传参给生成器函数，并执行一次迭代
print(gen.send(None))     #: 2        #: __next__() == send(None)
print("*" * 20)


def throw_gen():
    try:
        yield "Normal"
    except ValueError:
        yield "Error"
    finally:
        print("Finally")
gen = throw_gen()
print(gen.__next__())         #: Normal
# print(gen.__next__())         #: Finally, then StopIteration
print(gen.throw(ValueError))  #: Error    #: 传递 ValueError 异常给向生成器函数，并执行一次迭代
                              #: Finally
