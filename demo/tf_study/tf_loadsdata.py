#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-14 下午2:43"
import pymongo
import re
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')

def loadDataset():
    client = pymongo.MongoClient('47.88.244.133', 27017)
    db = client['dev_snippetnews']
    collection = db['news']
    docs = collection.find({'content_type': 'pic_content', 'addtime': {'$gt': 1530806400, '$lt': 1533522955}},
                           {'_id': 1, 'title': 1, 'content': 1})
    docList = []
    for doc in docs[:1000]:
        str = ''
        doc_one = filter_tags(str.join(doc['content']))
        docList.append(doc_one)
    return docList


def filter_tags(htmlstr):
    # 先过滤CDATA
    re_cdata = re.compile("//<!CDATA\[[>]∗//\]>", re.I)  # 匹配CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    re_br = re.compile('<br\s*?/?>')  # 处理换行
    re_h = re.compile('</?\w+[^>]*>')  # HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    s = re_cdata.sub('', htmlstr)  # 去掉CDATA
    s = re_script.sub('', s)  # 去去掉HTML注释掉SCRIPT
    s = re_style.sub('', s)  # 去掉style
    s = re_br.sub('\n', s)  # 将br转换为换行
    s = re_h.sub('', s)  # 去掉HTML 标签
    s = re_comment.sub('', s)  #
    # 去掉多余的空行
    blank_line = re.compile('\n+')
    s = blank_line.sub('\n', s)
    s = replaceCharEntity(s)  # 替换实体
    wordList = nltk.word_tokenize(s)
    wordList = [w for w in wordList if w not in stopwords.words('english')]  # 去除停用词
    s = ' '.join(wordList)
    return s


def replaceCharEntity(htmlstr):
    CHAR_ENTITIES = {'nbsp': ' ', '160': ' ',
                     'lt': '<', '60': '<',
                     'gt': '>', '62': '>',
                     'amp': '&', '38': '&',
                     'quot': '"''"', '34': '"', }
    re_charEntity = re.compile(r'&#?(?P<name>\w+);')
    sz = re_charEntity.search(htmlstr)
    while sz:
        entity = sz.group()  # entity全称，如>
        key = sz.group('name')  # 去除&;后entity,如>为gt
        try:
            htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
        except KeyError:
            # 以空串代替
            htmlstr = re_charEntity.sub('', htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
    return htmlstr


def repalce(s, re_exp, repl_string):
    return re_exp.sub(repl_string, s)


if __name__ == '__main__':
    loadDataset()