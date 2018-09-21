#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-11 下午3:03"

import tensorflow as tf
from numpy.random import RandomState
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 定义参数
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))
batch_size = 8
x = tf.placeholder(tf.float32, shape=(None, 2), name='x_input')
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y_input')  # 真实值
# 向前传播
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)  # 测试

# 定义损失函数和反向传播算法 交叉上函数
cross_entropy = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0)))
learning_rate = 0.001
# train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)
train_op = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cross_entropy)
# 生成数据
rdm = RandomState(1)
data_size = 128
X = rdm.rand(data_size, 2)
Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    steps = 5000
    for i in range(steps):
        start = (i * batch_size) % data_size
        end = min(start + batch_size, data_size)
        sess.run(train_op, feed_dict={x: X[start:end], y_: Y[start:end]})
        if i % 1000 == 0:
            total_cross_entroy = sess.run(
                cross_entropy, feed_dict={x: X, y_: Y}
            )
            print("after {} train steps,cross entropy on all data is {}" .format(i, total_cross_entroy))

