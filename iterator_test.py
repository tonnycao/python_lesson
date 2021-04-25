# -*- coding: utf-8 -*-
# @Time : 2021/4/25 11:03 下午
# @Author : tonnycao
# @Email : jian860129@126.com
# @File : iterator_test.py
# @Project : python_lesson

from collections.abc import Iterator


class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

if __name__ == '__main__':
    for key in Fab(5):
            print(key)