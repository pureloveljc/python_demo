# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/8/23 下午3:42"
import numpy as np


def softmax(a):
    c = np.max(a)  # 溢出对策
    x = np.exp(a-c)
    sum = np.sum(x)
    y = x / sum
    return y

value =  softmax(np.array([0.3, 2.9, 4.0]))
print(value)