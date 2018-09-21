# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/8/23 上午11:32"
import numpy as np
X = np.array([1, 2])
W = np.array([[1, 3, 6], [2, 4, 5]])

Y = np.dot(X, W)
print(Y)