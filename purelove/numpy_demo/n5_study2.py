# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/10/7 上午8:52"
import numpy as np
A = np.arange(2, 14).reshape((3, 4))
# print(A)
# print(np.argmin(A))  # 求最小值的索引
# print(np.argmax(A))  # 求最大值的索引
# print(np.mean(A))    # 求平均值
# print(np.average(A))  # 求平均值
# print(np.median(A))    # 中位数
# print(np.cumsum(A))  # 累加
# print(np.sort(A))  # 排序
# print(np.nonzero(A))  # 找到非0的索引
# print(np.transpose(A))  # 矩阵的转置
# print(A.T)  # 矩阵的转置
# print(A.T.dot(A))  # 很常用，转置之后相乘
# print(np.clip(A, 5, 10))   # 比5小都变成5，大于10的数都变成10
# print(np.mean(A, axis=0))  # axis=0对列进行计算 平均值   axis=1对于行进行计算
# 索引
print(A)
print(A[0])  # 0行
print(A[0][1])
print(A[0, 1])
print(A[2, :])  # 第二行所有的数
print(A[:, 1])  # 第一列的所有数
print(A[1, 1:2])  # 第一行当中 第一列到第二列的值
for row in A:  # 迭代每一行
    print(row)

for col in A.T:  # 迭代每一列
    print(col)

for item in A.flat:  # 迭代每一项
    print(item)
