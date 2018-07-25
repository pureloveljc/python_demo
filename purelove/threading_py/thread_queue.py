# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/7/22 下午4:17"
# 线程通信
import time
import threading
from threading_py import conf
# from threading_py.conf import detail_url_list  这样导入会有问题，其他的线程对变量的修改会出现问题
detail_url_list = []
#


def get_detail_html():
    global detail_url_list
    url = detail_url_list.pop()
    print("get detail html start")
    time.sleep(2)
    print("detail html end")


def get_detail_url(urdetail_url_listl):
    # 爬取列表页
    global detail_url_list
    print("get detail url start")
    time.sleep(2)
    for i in range(20):
        detail_url_list.append("http://www.baidu.com/{}".format(i))
    print("detail html end1")


if __name__ == '__main__':
    thread_detail_url = threading.Thread(target=get_detail_url, args=("",)) # 通过args进行参数传递
    thread_detail_html1 = threading.Thread(target=get_detail_html, args=("",))
    thread_detail_html2 = threading.Thread(target=get_detail_html, args=("",))
    thread_detail_html3 = threading.Thread(target=get_detail_html, args=("",))
    thread_detail_html4 = threading.Thread(target=get_detail_html, args=("",))
    thread_detail_html5 = threading.Thread(target=get_detail_html, args=("",))
    # 没有必这样开启5个，用for 循环
    for i in range(5):
        thread_detail_html1 = threading.Thread(target=get_detail_html, args=("",))
        thread_detail_html1.start()
    thread2 = threading.Thread(target=get_detail_url, args=("",))
    # thread1.setDaemon(True)  # thread设置为守护线程 当主线程退出后，会把thread1退出
    # thread2.setDaemon(True)
    start_time = time.time()
    # thread1.start()
    thread2.start()
    # 当主线程退出的时候，子线程会被kill掉
    # thread1.join()
    thread2.join() #等上面两个线程执行完成后再执行主线程
    print("last time: {}".format(time.time()-start_time))