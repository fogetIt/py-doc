#!/usr/bin/python3 env
#coding: utf-8
import sys
import time
import multiprocessing


def put_in_queue(Q):
    for i in range(10):
        Q.put(i)


def put_in_q1(Q):
    for i in range(10):
        Q1.put(i)


def pool_queue(func, Q):
    pool = multiprocessing.Pool()
    for i in range(5):
        pool.apply_async(func, args=(Q,))
    pool.close()
    pool.join()


def processes_queue(func, Q):
    for i in range(5):
        ps = multiprocessing.Process(target=func, args=(Q,))
        ps.start()
    for i in range(5):
        ps.join()


def main(P, func, Q):
    try:
        P(func, Q)
    except Exception as e:
        print(e)
    else:
        print(Q.qsize(), [Q.get() for i in range(Q.qsize())])


if __name__ == '__main__':
    Q1 = multiprocessing.Queue()
    Q2 = multiprocessing.Manager().Queue()
    """
    给子进程传参
    """
    main(processes_queue, put_in_queue, Q1)
    main(processes_queue, put_in_queue, Q2)
    main(pool_queue, put_in_queue, Q1)  # multiprocessing.Queue() is incorrect
    main(pool_queue, put_in_queue, Q2)
    """
    子进程引用父进程的全局变量
    """
    processes_queue(put_in_q1, 0)
    print(Q1.qsize(), [Q1.get() for i in range(Q1.qsize())])
    pool_queue(put_in_q1, 0)
    print(Q1.qsize(), [Q1.get() for i in range(Q1.qsize())])
