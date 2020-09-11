# -*- coding: UTF-8 -*-
import numpy as np

# 1.reshape() 函数用来改变向量的维度（不修改向量的本身）,可以只指定行数或列数，其他不想写可用-1表示，但是不能只指定行或列
a1 = np.arange(10)
a2 = a1.reshape(2, 5)
a3 = a1.reshape(5, -1)
a4 = a1.reshape(-1, 2)

# 2.resize()用于改变向量的维度，修改向量本身,需要先填入数组，然后再添加需要改变的形状
r1 = np.arange(10)
r2 = np.resize(r1, (2, 5))
r3 = r1.resize((5, 2))
# print(r3)

# 3.T属性用来对向量进行转置,只进行行数和列数的转换，仅此而已
t1 = np.arange(24).reshape(3, 8)
t2 = t1.T

# 4.ravel()函数用于向量展平,可以添加元素顺序变量，C顺序，即是按行方向顺序，照F顺序，即是列顺序重塑 A顺序，应该是针对于转置后的重塑
l1 = np.arange(24).reshape(4, -1)
l2 = l1.ravel('A')

# 5.flatten用来把矩阵转换成向量,相当于降维，三维数组到二维数组
f1 = np.random.random((3, 4))
f2 = f1.flatten()
f3 = f2.flatten()

# 6.squeeze()函数，也是用于数组降维，主要用于将矩阵中含1的维度去掉
s1 = np.arange(5).reshape(5, 1)
s2 = s1.shape
s3 = s1.squeeze().shape
s4 = np.arange(6).reshape(3, 1, 2, 1)
s5 = s4.shape
s6 = s4.squeeze().shape
s7 = s4.squeeze()

# 7.transpose函数，对高维矩阵进行轴对换
n1 = np.arange(24).reshape(2, 3, 4)
n2 = n1.transpose(1, 2, 0).shape
# print(n1)
# print(n2)

# 8.astype元素类型的变换
as1 = np.ones((2, 3, 4), dtype=np.int)
as2 = as1.astype(np.float)

# 9.tolist()数组向列表的转变
to1 = np.full_like((2, 3, 5), 2, dtype=np.int32)
to2 = to1.tolist()
print(to2)
