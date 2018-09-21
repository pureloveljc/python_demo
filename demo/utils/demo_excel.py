#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-6 下午1:30"
import json
import xlrd
import pprint

def readExcel():
    # 打开excel表单
    filename = u'/home/tf_demo/github_ljc/python_demo/finall对应假名字.xls'
    excel = xlrd.open_workbook(filename)

    # 得到第一张表单
    sheet1 = excel.sheets()[2]
    # 找到有几列几列
    nrows = sheet1.nrows  # 行数
    ncols = sheet1.ncols  # 列数

    totalArray = []
    title = []
    # 标题
    for i in range(0, ncols):
        title.append(sheet1.cell(0, i).value)

    # 数据
    for rowindex in range(1, nrows):
        dic = {}
        for colindex in range(0, ncols):
            s = sheet1.cell(rowindex, colindex).value
            dic[title[colindex]] = s
        totalArray.append(dic)

    return json.dumps(totalArray, ensure_ascii=False)


if __name__ == '__main__':

    vaule = readExcel()
    json_data = json.loads(vaule)
    # print(len(json_data))
    # print(json_data)
    for k in json_data:
        category = k['category_1'].split(',')
        dict1 = {"category_1": "new_youtube"}
        dict2 = {"category_2": category[1]}
        dict3 = {"category_3": category[2]}
        k.update(dict1)
        k.update(dict2)
        k.update(dict3)
    print(json.dumps(json_data))

