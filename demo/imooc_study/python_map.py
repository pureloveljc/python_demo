#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "18-7-23 上午9:39"

def add1(a):
    a+=1
    return a

v =  map(add1,[1,2,3,4])
print(list(v))

import re
a = re.findall('https://www.si.com/(.*?)/.*', 'https://www.si.com/mlb/2018/07/18/josh-hader-offensive-tweets')[0]
print(a)