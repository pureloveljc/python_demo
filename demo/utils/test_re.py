#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-8-22 下午4:45"
import numpy as np
import matplotlib.pyplot as plt
import re
url = 'https://www.crosswalk.com/family/singles/can-doctrinal-differences-make-you-unequally-yoked.html'
# pattern = re.compile(r'.*/\w+/[a-zA-Z]{1,}\d+/(\w+-){2,}\w+')
pattern = re.compile(r'https://www.crosswalk.com/\w+/[a-zA-Z\-]+/(\w+-){2,20}\w+.html$')
v = pattern.search(url)
print(v.group())
