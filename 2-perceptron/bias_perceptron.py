#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def AND (x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y  = AND(s1,s2)
    return y

def main():

    for xn in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        y = AND(xn[0], xn[1])
        print("AND"+str(xn) + " = " + str(y))

    for xn in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        y = NAND(xn[0], xn[1])
        print("NAND"+str(xn) + " = " + str(y))

    for xn in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        y = OR(xn[0], xn[1])
        print("OR"+str(xn) + " = " + str(y))

    for xn in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        y = XOR(xn[0], xn[1])
        print("XOR"+str(xn) + " = " + str(y))

if __name__ == '__main__':
    main()
