# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/9/5 下午10:28"
import requests
import json
headers = {'user agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                         '/39.0.2171.71 Safari/537.36'}
url = 'https://api.huobipro.com/market/history/kline?period=1min&size=2000&symbol=btcusdt' \
      '&AccessKeyId=71438159-5c9983b4-4e80f1ec-237a0'
resp = requests.get(url, headers=headers)
json_data = json.loads(resp.text)
print(resp.text)
