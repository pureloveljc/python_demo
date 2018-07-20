#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "18-7-17 上午11:36"

from collections import *
# 抽象基类
from collections.abc import *

user_dict = {}
users = ['a', 'b', 'a', 'c']

for u in users:
    user_dict.setdefault(u, 0)
    user_dict[u] += 1
print(user_dict)


def func(index):
    n = 0
    a = 0
    b = 1
    list1 = [0]
    while n < index:
        list1.append(b)
        a, b = b, a+b
        n += 1
    return list1

print(func(10))
