#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#出力層の設計
import numpy as np

def softmax_bf(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a/sum_exp_a
    return y

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) #オーバーフロー対策
    sum_exp_a = np.sum(exp_a)
    y = exp_a/sum_exp_a
    return y

def main():
    a = np.array([0.3, 2.9, 4.0])
    print(softmax(a))


if __name__ == '__main__':
    main()
