# -*- coding: UTF-8 -*-
import numpy as np

# 1.append()方法合并数组
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
a3 = np.append(a1, a2)  # 一维数组直接合并
a4 = np.arange(4).reshape(2, 2)
a5 = np.arange(4).reshape(2, 2)
a6 = np.append(a4, a5, axis=0)  # axis=0 则代表合并再列内，列数相加， axis=1行数相加

# 2.concatenate() 用法和append类似，沿指定轴连接数组或矩阵
c1 = np.array([[1, 2], [2, 3]])
c2 = np.array([[5, 6]])
c3 = np.concatenate((c1, c2), axis=0)
c4 = np.arange(4).reshape(2, 2)
c5 = np.arange(4).reshape(2, 2)
c6 = np.concatenate((c4, c5), axis=0)

# 3.stack()沿指定轴堆叠数组或矩阵
s1 = np.array([[1, 2], [3, 4]])
s2 = np.array([[5, 6], [7, 8]])
s3 = np.stack((s1, s2), axis=0)
print(s3)
