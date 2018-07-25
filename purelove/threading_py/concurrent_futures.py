# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/7/24 上午7:50"
from concurrent import futures

# 线程池，为什么要用线程池？
# 线程池管理更加容易
# 主线程中可以获取某一个线程的状态
# 当一个线程完成的时候我们主线程立即知道状态
# futures可以让多线程和多进程 编码接口一致
import time
from concurrent.futures import ThreadPoolExecutor


def get_html(times):
    time.sleep(times)
    print("go page {} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=10)
# 通过submit 函数提交执行的函数到线程池中
task1 = executor.submit(get_html, (3))
task2 = executor.submit(get_html, (2))

# done方法用于判定某个任务是否完成

print(task1.done())
print(task2.cancel())
time.sleep(3)
print(task1.done())
print(task1.result()) # result 得到执行的返回结果


# 比较初级