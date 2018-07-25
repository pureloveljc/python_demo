# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/7/22 下午10:46"

# 条件变量 用于复杂的线程间同步
from threading import Condition
import threading
import time


class Xiaoai(threading.Thread):
    def __init__(self, cond):
        self.cond = cond
        super().__init__(name="小爱")

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}:{}".format(self.name, "在"))
        # self.lock.release()
        # self.lock.acquire()
            self.cond.notify()
            self.cond.wait()
            print("{}:{}".format(self.name, "2"))
            self.cond.notify()
        # self.lock.release()


class Tianmao(threading.Thread):
    def __init__(self, cond):
        self.cond = cond
        super().__init__(name="天猫")

    def run(self):
        # self.lock.acquire()
        with self.cond:
            print("{}:{}".format(self.name, "小爱同学在不在"))
            self.cond.notify()  # 通知
            self.cond.wait()  # 等待
            # self.lock.acquire()
            print("{}:{}".format(self.name, "，小爱，1+1等于多少"))
            self.cond.notify()  # 通知
            self.cond.wait()  # 等待
            #self.lock.release()


class Main(threading.Thread):
    def __init__(self):
        super().__init__(name="main")

    def run(self):
        print("哈哈哈 我平时老大")

if __name__ == '__main__':
    cond = threading.Condition()
    xiaoai = Xiaoai(cond)
    tianmao = Tianmao(cond)
    # main = Main()
    xiaoai.start()  # 启动顺序很重要  在调用with之后才能调用 wait ,notify
    tianmao.start()

    # main.start()
    start_time = time.time()
# 验证了serDeamon(True)后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程均停止。


    xiaoai.join()
    tianmao.join()
    print("this is a main  {}".format(time.time()-start_time))
