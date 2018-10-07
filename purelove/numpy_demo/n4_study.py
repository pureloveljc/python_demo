# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/10/7 上午8:30"
import numpy as np
a = np.array([10, 20, 30, 40])
b = np.arange(4)
c = (a-b)**2
d = c.reshape((2, 2))
e = b.reshape((2, 2))
print(d)
print(e)
f = np.dot(d, e)  # 矩阵乘法  或者 f = d.dot(e)
g = d*e  # 对应位置逐个相乘
print(f)
print(g)


d = np.sin(a)  # np.cos(a)
print(d)
print(a < 30)
print(a == 30)
a = np.random.random((2, 4))
print(a)
print(np.sum(a, axis=0))  #axis=1 每一行中，中 axis=1，我们将得到按行计算的均值    axis=0是列
print(np.min(a))
print(np.max(a))
