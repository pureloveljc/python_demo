#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "18-7-16 下午4:57"
info = {}
N = input("请输入一个正整数:")
for x in range(N):
     a, b = map(int, (raw_input("Input a,b:")).split())
     if a in info:
         info[a] = info[a]+b
     else:
         info[a] = b
print(info)
max = 0
max_id = 0
for key in info:
    if info[key] > max:
        max = info[key]
        max_id = key
print('%s, %d' %(max_id, max))
