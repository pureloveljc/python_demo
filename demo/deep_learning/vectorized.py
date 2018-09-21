# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/8/28 下午9:34"
import time
import numpy as np

w = np.random.rand(100000)
# print(w)
x = np.random.rand(100000)
#print(x)
b = np.array([1])
start = time.time()
z = np.dot(w, x)
print(z.shape)
end = time.time()
print(z)
print((end-start)*1000)