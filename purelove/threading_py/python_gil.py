# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/7/21 下午9:15"
# 进程是竞争计算机资源的一个单位
# 一个cpu同一时刻只能执行一个进程  由于cpu运算速度非常快，
# cpu在不同的应用程序切换，让我们感受到同一时刻好像同时在运行
# 多核cpu同一时刻可以运行多个进程，算法决定哪个应用程序会被挂起，操作系统原理
# 进程/线程
# 线程比进程重要的多，线程是进程的一部分，一个进程 可以有1个线程也可以有多个线程
# 有进程来管理的话，不能有效来管理cpu的高性能，进程的切换非常消耗资源，
# 线程比进程更加灵活，轻量，减少了上下文管理，上下文切换是保存当前进程的状态
# 线程是进程的一部分，线程和进程分工不同，进程分配资源（内存资源，显卡资源等），线程利用cpu执行代码。
# 代码会变成一个一个指令，被cpu执行，线程本身不拥有也不管理资源，但是可以访问进程的资源
# python中一个线程对应一个c语言中的一个线程
# gil同一时刻 只有一个线程在一个cpu上执行字节码
import threading
import time


def working():
    print("i am chir thread")  # 3
    t = threading.current_thread()
    time.sleep(10)
    print(t.getName())  # 4


new_t = threading.Thread(target=working, name="ljc chir thrad")
new_t.start()

print("i am ljc")  # 1
t = threading.current_thread()
a = 1
a = a+1
print(t.getName())  # 2
# 多线程可以利用cpu多核的性能优势
# 单核cpu同一时刻只能执行一个线程
# 单核CPU电脑同一时间内只能执行一个线程,这句话是对的,
# python 没有办法利用多核cpu的优势！！！！！！！
# python的多线程是鸡肋？？
# python 的多线程
# 全局解释器锁 gil的存在python没有办法利用多核cpu
# gil的存在同一时刻只能在一个核上面执行一个线程
# 全局解释器锁，线程安全 进程管理资源，线程访问进程资源
# 一个进程有多个线程 共享资源，多个线程访问资源，线程不安全
# a=3 main
# A线程 a+=1  print(a)
# B线程 a+=4  print(a)
# 结果就是 可能先执行A, 可能先执行B，多线程的话，千万不要认为代码写在面前，先执行
# 锁的机制，只有拿到锁的线程，比如A拿到锁，先执行代码，如果不释放，那么B就不能执行。
# 谁拿到锁就先执行
# 细粒度锁  程序员在代码里面加的锁
# 粗粒度锁 gil,解释器层面加一个锁，全局解释器锁
# gil的存在只允许同一时刻只能在一个核上面执行一个线程，一定程度上保证线程安全！
# 解释器 bytecode
# 开启多进程可以利用多核cpu 缺点就是进程之间资源共享，要用进程通信技术，而且进程切换是相当消耗资源
# I/O密集型程序，python多线程是有意义的
# 假设10个线程，非常严重的依赖cpu计算，cpu密集型程序。多线程意义不大
# 大多数是I/O密集型程序，查询数据库，发送http请求，读写文件都是I/O操作，多线程是有意义的
# 密集的概念绝大部分时间都花在执行查询，时间段消耗在什么样的操作上面