# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/10/7 上午10:34"
import numpy as np
import pandas as pd

# numpy序列化之后的矩阵， pandas中更像一个字典形式的numpy
# 主要两个数据结构：Series和DataFrame

# s = pd.Series([1, 2, 3, 4, 'ljc', 'love', ' you'])
# print(s)
# d = pd.Series([1, 2, 3, 4])
# print(d)

data = pd.date_range('20181007', periods=6)  # 生成6个日期
print(data)
df = pd.DataFrame(np.random.rand(6, 4), index=data, columns=['a', 'b', 'c', 'd'])
# 6行  4列， 行的columns  index列的索引
print(df)
df1 = pd.DataFrame(np.arange(12).reshape(3, 4))  # 不指定index 则默认生成
print(df1)
df2 = pd.DataFrame({'a': 'ljc', 'b': 'love'}, index=data)
print(df2)

df3 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df3)
print(df3.columns)
print(df3.values)
print(df3.sort_values(by='B'))   # 对树值 排序输出: