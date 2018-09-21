#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-17 上午10:58"
import tensorflow as tf

v1 = tf.Variable(0, dtype=tf.float32)

step = tf.Variable(0, trainable=False)

ema = tf.train.ExponentialMovingAverage(0.99, step)

maintain_averages_op = ema.apply([v1])

with tf.Session() as sess:
    init = tf.initialize_all_variables()
    sess.run(init)

    print(sess.run([v1, ema.average(v1)]))