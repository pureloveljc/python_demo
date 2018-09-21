#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-12 上午11:40"
import tensorflow as tf
import tensorflow.contrib as contrib

weight = tf.constant([[1.0, -2.0], [-3.0, 4.0]])
with tf.Session() as sess:
    # 输出为(|1|+|-2|+|-3|+|4|)*0.5=5
    print(sess.run(contrib.layers.l1_regularizer(0.5)(weight)))
    # 输出为(1²+(-2)²+(-3)²+4²)/2*0.5=7.5
    # TensorFlow会将L2的正则化损失值除以2使得求导得到的结果更加简洁
    print(sess.run(contrib.layers.l2_regularizer(0.5)(weight)))
    # l1_regularizer+l2_regularizer
    print(sess.run(contrib.layers.l1_l2_regularizer(0.5, 0.5)(weight)))
