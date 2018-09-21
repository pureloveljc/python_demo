#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-3 上午9:46"
import requests
import json
headers = {'user agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
url_s1 = 'https://api.huobipro.com/market/history/kline?period=1day&size=2000&symbol=btcusdt&AccessKeyId=fff-xxx-ssss-kkk'
resp = requests.get(url_s1, headers=headers, timeout=5)
print(resp.text)
json_data = json.loads(resp.text)
# print(json_data)