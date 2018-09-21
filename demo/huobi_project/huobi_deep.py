#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-19 下午4:08"
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ——————————————————导入数据——————————————————————
f = open('/home/tf_demo/github_ljc/python_demo/demo/huobi_project/data2018-09-19.csv')
df = pd.read_csv(f)  # 读入股票数据
data = np.array(df['high'])  # 获取最高价序列
data = data[::-1]  # 反转，使数据按照日期先后顺序排列

print(data)
batch_size = 60
x = tf.placeholder(tf.float32, [None, 1], name='x-input')
y_ = tf.placeholder(tf.float32, [None, 1], name='y_input')
w = tf.Variable(tf.random_normal([1, 1], stddev=1, seed=1))
# b = tf.Variable(tf.random_normal([1], stddev=1, seed=1))
b = tf.get_variable('b', [1], initializer=tf.constant_initializer(0.0))
y = tf.matmul(x * w) + b
loss = tf.reduce_mean(tf.square(y, y_))
train_op = tf.train.AdamOptimizer(0.0001).minimize(loss)
with tf.Session() as sess:
    init = tf.initialize_all_variables()
    sess.run(init)
    step = 10000
    for i in range(step):
        pass
