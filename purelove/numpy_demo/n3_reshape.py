# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/8/26 上午10:28"
import numpy as np
a = np.array(range(30)).reshape(2, 3, 5)
print(a)
print('～～～～～'*10)
print(a[0][2][1])
print('～～～～～'*10)
print(a.transpose(1, 0, 2))
# 元素11在a中的位置是a[0][2][1]，经过b = a.transpose(1, 0, 2)之后，11在b中的位置就变成b[2][0][1]
# A.transpose((0,1,2))  #保持A不变
# A.transpose((1,0,2))  #将 0轴 和 1轴 交换
