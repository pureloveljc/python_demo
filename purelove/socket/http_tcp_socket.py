# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/7/19 上午7:57"

# 应用层(http,ftp,smtp等) ->传输层（tcp,udp协议 提供端对端的借口） 网络层(ip协议，)-> 数据链路层(传输地址的桢)-> 物理层（物理媒体）
# A客户端 对B 发送请求  经过5层网络
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()
sock, addr = server.accept()
date = server.recv(1024)
