# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "2018/8/23 上午11:59"
import numpy as np
def sigmoid(x):
    return 1/(1 + np.exp(-x))

def init_network():
    network = {}
    network['W1'] = np.array([[0.2, 0.3, 0.4], [0.1, 0.4, 0.3]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.2, 0.3], [0.1, 0.4], [0.2, 0.4]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.2, 0.3], [0.1, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network


def forward(net_work, x):
    w1, w2, w3 = net_work['W1'], net_work['W2'],  net_work['W3']
    b1, b2, b3 = net_work['b1'], net_work['b2'],  net_work['b3']
    a1 = np.dot(x, w1)+b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, w2)+b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, w3)+b3
    # y = indey_func(a3)
    return a3
net_work = init_network()
x = np.array([1.0, 0.5])
y = forward(net_work, x)
print(y)