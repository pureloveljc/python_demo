# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/8/25 下午11:41"
import numpy as np

x = np.arange(12)
print(x)
print(type(x))
print(x.shape)
print('~~~~~~~~~~'*10)
x = x.reshape(3, 4)
print(x)
print('~~~~~~~~~~'*10)
print(x.reshape(1, -1))
print(x.reshape(1, 12))
print(x.T)
print('~~~~~~~~~~'*10)
B = np.arange(24).reshape(2, 3, 4)
print(B)
print(B.reshape(1, 24))
