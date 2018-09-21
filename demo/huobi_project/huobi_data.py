#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-18 上午10:21"
import time
import xlwt
import requests
import json
import datetime
import pandas as pd


def write_excel(period):
    headers = {
        'user agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
    url_s1 = 'https://api.huobipro.com/market/history/kline?period={}&size=2000&' \
             'symbol=btcusdt&AccessKeyId=fff-xxx-ssss-kkk'.format(period)
    resp = requests.get(url_s1, headers=headers, timeout=5)
    json_data = json.loads(resp.text).get('data')
    title = ["time", "open", "close", "low", "high", "amount", "vol", 'count']
    book = xlwt.Workbook()  # 创建一个excel对象
    sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)  # 添加一个sheet页
    for i in range(len(title)):  # 循环列
        sheet.write(0, i, title[i])  # 将title数组中的字段写入到0行i列中]
    count = 1
    for d in json_data:  # 循环字典
        timeStamp = int(d['id'])
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        sheet.write(count, 0, otherStyleTime)  # 将line写入到第int(line)行，第0列中
        sheet.write(count, 1, d['open'])
        sheet.write(count, 2, d['close'])
        sheet.write(count, 3, d['low'])
        sheet.write(count, 4, d['high'])
        sheet.write(count, 5, d['amount'])
        sheet.write(count, 6, d['vol'])
        sheet.write(count, 7, d['count'])
        count += 1
    path = 'data{}.xls'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    path_csv = 'data{}.csv'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    book.save(path)
    data_xls = pd.read_excel(path, index_col=0)
    data_xls.to_csv(path_csv, encoding='utf-8')


if __name__ == '__main__':
    """period  1min, 5min, 15min, 30min, 60min, 1day, 1mon, 1week, 1year"""
    write_excel('60min')
