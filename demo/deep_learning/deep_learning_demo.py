# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/8/23 上午10:15"
import numpy as np
import matplotlib.pylab as plt

# def sigmoid(x):
#     return 1/(1 + np.exp(-x))
#
# x = np.arange(-5, 5, 0.1)
# y = sigmoid(x)
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1)  # y范围
# plt.show()

a = np.array([[3, 4],
              [5, 6],
              [7, 8]])

b = np.array([[1, 2, 3, 5], [6, 8, 9, 0]])
print(a.shape)
print(b.shape)
print(np.dot(a, b))  # 矩阵的乘法
