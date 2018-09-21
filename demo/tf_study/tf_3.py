#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-13 下午8:13"
import tensorflow as tf
import tensorflow.contrib as contrib


def get_weight(shape, lambd):
    var = tf.Variable(tf.random_normal(shape), dtype=tf.float32)
    tf.add_to_collection('losses', contrib.layers.l2_regularizer(lambd)(var))
    return var


x = tf.placeholder(tf.float32, shape=[None, 2])
y_ = tf.placeholder(tf.float32, shape=[None, 1])
batch_size = 8  # 一般是2个N次方
layer_dimension = [2, 10, 10, 10, 1]
# 神经网络层数
n_layers = len(layer_dimension)
cur_layer = x
in_demension = layer_dimension[0]

for i in range(1, n_layers):
    out_dimension = layer_dimension[i]
    weight = get_weight([in_demension, out_dimension], 0.001)
    bias = tf.Variable(tf.constant(0.1, shape=[out_dimension]))
    cur_layer = tf.nn.relu(tf.matmul(cur_layer, weight)+bias)
    in_demension = layer_dimension[i]

mse_loss = tf.reduce_mean(tf.square(y_-cur_layer))
tf.add_to_collection('losses', mse_loss)
loss = tf.add_n(tf.get_collection('losses'))
