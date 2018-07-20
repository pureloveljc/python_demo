#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "18-7-16 下午8:48"

# 微信抢红包查看数量
def wexin(list1):
    dict1 = {}
    for i in list1:
        if i not in dict1.keys():
            dict1[i] = 1
        else:
            dict1[i] += 1
    list2 = []
    list3 = []
    for k, v in dict1.items():
        list2.append(v)
        list3.append(k)
    a = [i for i in list2 if i > len(list1) / 2]
    if a:
        return list(dict1.keys())[list(dict1.values()).index(a[0])]
    else:
        return 0


if __name__ == '__main__':
    list1 =[1,1,2,2,2,2,1,1,1,2,2,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
    v = wexin(list1)
    print(v)