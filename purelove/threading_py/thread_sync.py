# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/7/22 下午6:46"
# 线程同步

from threading import Lock, RLock
import threading

total = 0
lock = RLock()  # 锁
# 锁会影响性能
# 锁会引起死锁
# 死锁情况 A(a,b) acquire(a) ,acquire(b)
# B(a,b) acquire(b) , acquire(a)
# Rlock在同一个线程里面可以连续调用多次acquire
# 一定要注意acquire的次数和release的次数相等


def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        lock.acquire() #死锁
        total += 1
        lock.release()
        lock.release()
    return total


def desc():
    global total
    # global lock
    for i in range(1000000):
        lock.acquire()  # 获取锁
        total -= 1
        lock.release()  # 释放锁

    return total



thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(total)
