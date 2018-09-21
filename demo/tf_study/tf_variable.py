#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-17 下午4:10"
import tensorflow as tf


def inference(input_tensor, reuse=False):
    # 变量管理
    with tf.variable_scope('layer1', reuse=reuse):
        weights = tf.get_variable("weights", [input_node, layer1_node],
                                  initializer=tf.truncated_normal_initializer(stddev=0.1))
        biases = tf.get_variable("biases", [layer1_node])
        layers1 = tf.nn.relu(tf.matmul(input_tensor, weights)+biases)

    with tf.variable_scope('layer2', reuse=reuse):
        weights = tf.get_variable("weights", [layer1_node, out_node],
                                  initializer=tf.truncated_normal_initializer(stddev=0.1))
        biases = tf.get_variable("biases", [out_node])
        layers2 = tf.nn.relu(tf.matmul(layers1, weights)+biases)

    return layers2


x = tf.placeholder(tf.float32, shape=[None, input_node], name='x_input')
y = inference(x)