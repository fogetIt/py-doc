#!/usr/bin/python3 env
import multiprocessing
import time


def queue_option(Q):
    for i in range(5):
        if Q.empty():
            Q.put(1)
        else:
            Q.put(Q.get() + 1)



if __name__ == '__main__':
    # multiprocessing.Queue() is incorrect
    Q = multiprocessing.Manager().Queue()
    pool = multiprocessing.Pool()
    for i in range(5):
        pool.apply_async(queue_option, args=(Q,))
    pool.close()
    pool.join()
    print(Q.qsize())
    print([Q.get() for i in range(Q.qsize())])
