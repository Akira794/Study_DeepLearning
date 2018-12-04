#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#活性化関数

import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int)

def sigmoid_function(x):
    return 1/(1+np.exp(-x))

def relu_function(x):
    return np.maximum(0,x)

def main():

    x = np.arange(-5.0, 5.0, 0.1)

    step_y = step_function(x)
    sigmoid_y = sigmoid_function(x)
    relu_y = relu_function(x)

    plt.plot(x, step_y, linestyle="dashed", label="$step$")
    plt.plot(x, sigmoid_y, 'r-', label="$sigmoid$")
    plt.plot(x, relu_y, 'g-', label="$relu")
    plt.xlim(-6.0, 6.0)
    plt.ylim(-0.1, 1.1) #y range
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
