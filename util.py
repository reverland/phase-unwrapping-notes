#! /bin/env python
# -*- coding: utf8 -*-

import numpy as np
# import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


# wrap function
def wrap(x):
    return np.arctan2(np.sin(x), np.cos(x))


# unwrap function
def wrap_diff(x):
    return wrap(np.diff(x))


# one dimensional unwrap
def raster_unwrap(x):
    """one dimensional unwrap for itoh's raster algrithom"""
    y = x
    y[0] = x[0]
    for i in range(len(x) - 1):
        i += 1
        y[i] = y[i - 1] + wrap_diff(x)[i - 1]
    return np.array(y)


# two dimensional unwrap
def raster_unwrap2(Z):
    """raster two dimensional unwrapping algrithom based on itoh's"""
    A = Z.copy()
    A[:, 0] = raster_unwrap(A[:, 0])
    for j in range(np.size(A, axis=0)):
        A[j, :] = raster_unwrap(A[j, :])
    return A


# noisy test_data
def noisy_test_data(num):
    X, Y, Z = axes3d.get_test_data(0.05)

    x = np.random.randint(0, Z.shape[0], num)
    y = np.random.randint(0, Z.shape[1], num)
    for i, j in zip(x, y):
        Z[i, j] = np.random.random_sample() * 8
    return Z
