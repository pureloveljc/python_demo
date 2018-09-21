#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "tf_demo"
__date__ = "18-9-17 下午5:18"
import tensorflow as tf
# 回归问题一般用均方
mse = tf.reduce_mean(tf.square(y,y_))