#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-14 下午5:27"
import tensorflow as tf
import tensorflow.contrib as contrib


def get_weight(shape, lambd):
    var = tf.Variable(tf.random_normal(shape), dtype=tf.float32)
    tf.add_to_collection('losses', contrib.layers.l2_regularizer(lambd)(var))
    return var


x = tf.placeholder(tf.float32, shape=[None, 2], name='x_input')
y_ = tf.placeholder(tf.float32, shape=[None, 1], name='y_input')
batch_size = 8
layer_dimension = [2, 10, 10, 10, 1]  # 每一层网络中的节点
n_layers = len(layer_dimension)

cut_layer = x
in_dimension = layer_dimension[0]

for i in range(1, n_layers):
    out_dimension = layer_dimension[i]
    weight = get_weight([in_dimension, out_dimension], 0.001)
    bias = tf.Variable(tf.constant(0.1, shape=[out_dimension]))
    cur_layer = tf.nn.relu(tf.matmul(x, weight)+bias)
    in_dimension = layer_dimension[i]

mse_loss = tf.reduce_mean(tf.square(y_-cur_layer))