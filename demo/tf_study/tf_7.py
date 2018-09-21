#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-20 下午3:49"
import tensorflow as tf

x = tf.constant([[0.7, 0.9]], dtype=tf.float32)
w1 = tf.constant([[2, 3, 4], [2, 3, 6]], dtype=tf.float32)
w2 = tf.constant([[3, 2], [1, 2], [4, 6]], dtype=tf.float32)
w3 = tf.constant([[2], [1]], dtype=tf.float32)
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)
z = tf.matmul(y, w3)
sess = tf.Session()
init = tf.global_variables_initializer()
value = sess.run(init)
print(sess.run(z))
sess.close()
