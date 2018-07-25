# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/7/22 下午6:14"

# 通过queue 的方式来进行线程同步
from queue import Queue
import time
import threading

def get_detail_html(queue):
    # 爬取文章详情页
    url = queue.get()
    # for url in detail_url_list:
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")
    queue.task_done()


def get_detail_url(queue):
    # 爬取文章列表页
    print("get detail url started")
    # time.sleep(4)
    for i in range(5):
        queue.put("http://projectsedu.com/{id}".format(id=i))
    print("get detail url end")


# 1. 线程通信方式- 共享变量

if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)

    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    thread_detail_url.start()
    for i in range(6):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()
    # # thread2 = GetDetailUrl("get_detail_url")
    start_time = time.time()

    # thread_detail_url1.start()
    #
    # thread1.join()
    # thread2.join()
    # detail_url_queue.task_done()
    detail_url_queue.join()

    # 当主线程退出的时候， 子线程kill掉
    print("last time: {}".format(time.time() - start_time))