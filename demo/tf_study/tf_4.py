#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-14 上午10:45"
import tensorflow as tf
import tensorflow.contrib as contrib

w = tf.constant([[3, 4, 5], [7, 8, 9]])
batch_size = 8
x = tf.placeholder(tf.float32, [batch_size, 2], name='x_input')
y_ = tf.placeholder(tf.float32, [batch_size, 1], name='y_input')
w = tf.Variable(tf.float32, tf.random_normal([2, 3]))
y = tf.matmul(x, w)
global_step = 1000

learning_rate = tf.train.exponential_decay(0.1, global_step, 100, 0.96, staircase=True)
loss = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0)))+contrib.layers.l2_regularizer(w)
train_op = tf.train.AdamOptimizer(learning_rate).minimize(loss)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    for i in range(global_step):
        sess.run(train_op, feed_dict={x: '', y_: ''})
