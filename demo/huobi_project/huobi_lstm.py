#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-18 上午10:37"
import tensorflow as tf
import pandas as pd
import numpy as np

# 数据处理
path = '/home/tf_demo/github_ljc/python_demo/demo/huobi_project/data2018-09-18 10:35.csv'
api_data = pd.read_csv(path)
result = api_data.head()
data = result.iloc[:, 3:8].values
print(data)

rnn_unit = 20  # 隐藏单元
input_size = 1  # 输入层维度
output_size = 1  # 输出层维度
learing_rate = 0.0006
tf.reset_default_graph()  # 利用这个可清空defualt graph以及nodes

weight = {
    'in': tf.Variable(tf.random_normal([input_size, rnn_unit])),
    'out': tf.Variable(tf.random_normal([rnn_unit, 1]))
}
biases = {
    'in': tf.Variable(tf.constant(0.1, shape=[rnn_unit, ])),
    'out': tf.Variable(tf.constant(0.1, shape=[1, ]))
}


def get_data(batch_size=124, time_step=20, train_begin=0, train_end=2000):
    pass


# ——————————————————定义神经网络变量——————————————————


def lstm_network(X):
    batch_size = tf.shape(X)[0]
    time_step = tf.shape(X)[1]
    w_in = weight['in']
    b_in = biases['in']
    input = tf.reshape(X, [-1, input_size])
    input_rnn = tf.matmul(input, w_in) + b_in
    input_rnn = tf.reshape(input_rnn, [-1, time_step, rnn_unit])
    cell = tf.nn.rnn_cell.BasicLSTMCell(rnn_unit)
    init_state = cell.zero_state(batch_size, dtype=tf.float32)
    output_rnn, final_states = tf.nn.dynamic_rnn(cell, input_rnn, initial_state=init_state,
                                                 dtype=tf.float32)  # output_rnn是记录lstm每个输出节点的结果，final_states是最后一个cell的结果
    output = tf.reshape(output_rnn, [-1, rnn_unit])  # 作为输出层的输入
    w_out = weight['out']
    b_out = biases['out']
    pred = tf.matmul(output, w_out) + b_out
    return pred, final_states


# ——————————————————训练模型——————————————————

def train_lstm(batch_size=80, time_step=15, train_begin=0, train_end=2000):
    X = tf.placeholder(tf.float32, shape=[None, time_step, input_size])
    Y = tf.placeholder(tf.float32, shape=[None, time_step, output_size])

    loss = tf.reduce_mean(tf.square(tf.reshape()))
