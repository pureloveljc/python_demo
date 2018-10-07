# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/10/7 上午9:26"
import numpy as np
# A = np.array([1, 1, 1])
# B = np.array([2, 2, 2])
# print(np.vstack((A, B)))  # 上下合并
# print(np.hstack((A, B)))  # 左右合并
# print(A.reshape(3, 1))
# print(A[:, np.newaxis])  # 在列上增加一个纬度 # 如何用横向数列 变成 竖向数列
# print(A[np.newaxis, :])  # 在行上增加一个纬度
# x = np.concatenate((A, B, B, A), axis=0)   # 多个数组的合并
# print(x)
 # 分割
A = np.arange(12).reshape(3, 4)
a, b = np.split(A, 2, axis=1)  # 对A进行分割成2块，在行上
print(np.array_split(A, 3, axis=1))  # 不等分割
print(b)
print(np.vsplit(A, 3))  # 纵向分割
print(np.hsplit(A, 2))  # 横向分割
B = A.copy()  # 把A的值 copy给B, 但是两者不关联  但是等号赋值B=A 则会关联，即改变A的值，B也会随之改变
print(B)
