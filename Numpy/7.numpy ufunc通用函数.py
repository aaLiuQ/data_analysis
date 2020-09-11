# -*- coding: UTF-8 -*-
import math
import numpy as np
import time

# numpy的内建函数来实现计算的向量化，可以提高运行速度
x1 = np.random.rand(1000000)
x2 = np.random.rand(1000000)
# 使用循环计算向量点积
tic = time.process_time()
com = 0

for i in range(len(x1)):
    com += x1[i] * x2[i]

toc = time.process_time()

print("dot = " + str(com) + "\n for loop----- Computation time = " + str(1000*(toc - tic)) + "ms")

# 使用numpy函数求点积
tic = time.process_time()

dot = np.dot(x1,x2)
toc = time.process_time()

print("dot = " + str(dot) + "\n verctor version---- Computation time = " + str(1000*(toc - tic)) + "ms")
