# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/7/22 上午11:29"
# 锁会释放，不会整个过程都占有，比如执行字节码1000行之后会
# 比如执行字节码1000行之后会，释放锁，整个线程不会一直占有
# 或者执行15毫秒之后（时间片）会释放
# 遇到I/O操作的时候会主动释放
# 遇到I/O密集型的程序时是非常必要的

total = 0


def add():
    global total
    for i in range(1000000):
        total += 1
    return total

def desc():
    global total
    for i in range(1000000):
        total -= 1
    return total


import threading

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(total)