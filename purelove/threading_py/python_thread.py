# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/7/22 上午11:24"
# gil的存在只允许同一时刻只能在一个核上面执行一个线程，一定程度上保证线程安全！
# gil的存在只允许同一时刻只有一个线程执行在一个cpu上执行字节码
# 无法将多个线程映射到多个cpu上
import dis


def add(a):
    a = a+1
    return a

print(dis.dis(add))
