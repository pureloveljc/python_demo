# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/8/31 下午11:46"
import tensorflow as tf

x = tf.placeholder(tf.float32, [None, 3072])  # 输入data None输入样本的数量是不确定的[3,1,2]
# y[None]
y = tf.placeholder(tf.int64, [None])  # label 离散变量所以用int64  标签
# w (3027,1）
w = tf.get_variable('w', [x.get_shape()[-1], 1],
                    initializer=tf.random_normal_initializer(stddev=0.02))  # 正太分布，均值是0，方差

print(x.get_shape()[-1])
