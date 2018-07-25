# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/7/22 上午11:41"
import threading
import time


def get_detail_html(url):
    print("get detail html start")
    time.sleep(2)
    print("detail html end")


def get_detail_url(url):
    print("get detail url start")
    time.sleep(2)
    print("detail html end1")


# if __name__ == '__main__':
#     thread1 = threading.Thread(target=get_detail_html, args=("",))
#     thread2 = threading.Thread(target=get_detail_url, args=("",))
#     thread1.setDaemon(True)  # thread设置为守护线程 当主线程退出后，会把thread1退出
#     # thread2.setDaemon(True)
#     start_time = time.time()
#     thread1.start()
#     thread2.start()
#     # 当主线程退出的时候，子线程会被kill掉
#     thread1.join()
#     thread2.join() #等上面两个线程执行完成后再执行主线程
#     print("last time: {}".format(time.time()-start_time))


class GetdetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
    def run(self):
        print("get detail html start")
        time.sleep(2)
        print("detail html end")
        a = self.go()
        print(a)

    def go(self):
        list1 = [1,2,3]
        return  list1


class Getdetailurl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url start")
        time.sleep(4)
        print("detail html end1")


if __name__ == '__main__':
    # thread1 = threading.Thread(target=get_detail_html, args=("",))
    # thread2 = threading.Thread(target=get_detail_url, args=("",))
    # thread1.setDaemon(True)  # thread设置为守护线程 当主线程退出后，会把thread1退出
    # # thread2.setDaemon(True)
    # start_time = time.time()
    # thread1.start()
    # thread2.start()
    # # 当主线程退出的时候，子线程会被kill掉
    # thread1.join()
    # thread2.join() #等上面两个线程执行完成后再执行主线程
    # print("last time: {}".format(time.time()-start_time))
    thread1 = GetdetailHtml("get_detail_html")
    thread2 = Getdetailurl("get_detail_url")
    start_time = time.time()
    thread1.start()
    thread2.start()
    # # 当主线程退出的时候，子线程会被kill掉
    thread1.join()
    thread2.join() #等上面两个线程执行完成后再执行主线程
    print("last time: {}".format(time.time()-start_time))
