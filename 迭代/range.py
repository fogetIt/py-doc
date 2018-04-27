# -*- coding: utf-8 -*-
# @Date:   2018-03-16 09:12:48
# @Last Modified time: 2018-03-16 09:13:31


class Range(object):

    def __init__(self, start, stop=0, step=1):
        self.start = start if stop else 0
        self.stop = stop if stop else start
        self.step = step
        self.index = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.stop:
            temp = self.index
            self.index += self.step
            return temp
        raise StopIteration


if __name__ == '__main__':
    r = Range(10)
    print(r)
    for i in r:
        print(i, end=" ")
    print("---")
    for i in r:
        print(i, end=" ")
