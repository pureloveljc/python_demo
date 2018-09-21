#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-21 上午10:27"
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow.contrib as contrib

input_node = 784
output_node = 10
layer1_node = 500
batch_size = 100
learing_rate_base = 0.8
learing_decay = 0.99
regularization_rate = 0.0001  # 正则化在损失函数中的系数
training_steps = 30000
moving_average_decay = 0.99  # 滑动平均衰减


def inference(input_tensor, avg_class, weight1, bias1, weight2, bias2):
    if avg_class == None:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weight1) + bias1)
        layer2 = tf.nn.relu(tf.matmul(layer1, weight2) + bias2)
        return layer2
    else:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, avg_class.average(weight1)) + avg_class.average(bias1))
        layer2 = tf.nn.relu(tf.matmul(layer1, avg_class.average(weight2)) + avg_class.average(bias2))
        return layer2


def train(mnist):
    x = tf.placeholder(tf.float32, shape=(None, input_data), name='x_input')
    y_ = tf.placeholder(tf.float32, shape=(None, output_node), name='y_output')
    weights1 = tf.Variable(tf.truncated_normal([input_data, layer1_node], stddev=0.1))
    biases1 = tf.Variable(tf.constant(0.1, shape=[layer1_node]))
    weights2 = tf.Variable(tf.truncated_normal([layer1_node, output_node], stddev=0.1))
    biases2 = tf.Variable(tf.constant(0.1, shape=[output_node]))
    y = inference(x, None, weights1, biases1, weights2, biases2)
    global_step = tf.Variable(0, trainable=False)  # 训练论数的变量,指定为不可训练参数
    # 滑动平均衰减率 和训练论数的变量, 初始化滑动平均类
    # 给定训练轮数的变量可以加快训练早期变量的速度
    variable_averages = tf.train.ExponentialMovingAverage(moving_average_decay, global_step)
    variable_averages_op = variable_averages.apply(tf.trainable_variables())
    # 滑动平均不会改变变量本身的取值,而是会维护一个影子变量记录其滑动平均值, 所以需要使用滑动平均值时候,需要明确调用average函数
    average_y = inference(x, variable_averages, weights1, biases1, weights2, biases2)
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(y, tf.argmax(y_, 1))
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    regularizer = contrib.layers.l2_regularizer(regularization_rate)
    regularization = regularizer(weights1)+regularizer(weights2) # 一般不使用偏执
    loss = cross_entropy_mean+regularization
    # 学习率衰减
    learing_rate = tf.train.exponential_decay(learing_rate_base, global_step, mnist.train.num_examples/batch_size,
                                              learing_decay)
    train_step = tf.train.GradientDescentOptimizer(learing_rate).minimize(loss, global_step=global_step)
    # 在训练神经网络模型时,每过一遍数据需要通过反向传播更新网络中的参数,
    # 又要更新每一个参数的滑动平均值,为了一次完成多个操作,tensorflow提供 tf.control.dependencies和tf.group两种机制
    train_op = tf.group(train_step, variable_averages_op)
    correct_prediction = tf.equal(tf.argmax(average_y, 1), tf.argmax(y_, 1))
    # cast将布尔型数据转换成实数型
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    with tf.Session() as sess:
        tf.initialize_all_variables().run()
        validate_feed = {x: mnist.validation.images, y_: mnist.validation.labels}
        test_feed = {x: mnist.test.images, y_: mnist.test.labels}
        for i in range(training_steps):
            if i % 1000 == 0:
                validate_acc = sess.run(accuracy, feed_dict=validate_feed)
                print('After %d training steps,validation accuracy using average model is %g' % (i, validate_acc))
            xs, ys = mnist.train.next_batch(batch_size)
            sess.run(train_op, feed_dict={x: xs, y_: ys})
        test_acc = sess.run(accuracy, feed_dict=test_feed)
        print('After %d training steps,test accuracy using average model is %g' % (training_steps, test_acc))


def main(argv=None):
    mnist = input_data.read_data_sets('/tmp/data', one_hot=True)
    train(mnist)


if __name__ == '__main__':
    tf.app.run()
