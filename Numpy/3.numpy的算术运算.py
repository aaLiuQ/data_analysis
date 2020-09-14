# -*- coding: UTF-8 -*-
import numpy as np
import random

# 1.np.multiply()用来计算数组或矩阵的对应元素相乘，输出与相乘数组或矩阵的大小一致
a = np.array([[2, 5], [-5, -6]])
b = np.array([[4, 3], [9, 6]])
c = a * b
d = np.multiply(a, b)  # 等价于a*b，各个位置上的相乘
e = a + 2  # 也可以每个数值与单一数值加减乘除，这个数值也被称之为标量

# 2.通过函数进行运算
np.random.seed(20)
x = np.random.rand(4, 5)  # 生成4行5列的0-1的随机数
g = np.exp(x)  # 返回e的x次方，e为一个常数为2.71828 x为4行5列的0-1的随机数
f = 1 / (1 + np.exp(-x))
h = np.maximum(0.5, x)  # maximum()传入两个值，比较大小，比0.5大的留下，比0.5小的留0.5
j = np.sum(np.exp(x))
i = np.exp(x) / np.sum(np.exp(x))

# 3.点积运算，又称内积，用np.dot()函数表示
a1 = np.dot(5, 8)  # 如果只是两个数则是直接相乘

a2 = np.array([2, 3, 5])
a3 = np.array([3, 4, 6])
a4 = np.dot(a2, a3)  # 如果是相同数量的一维数组，则是两两相乘取和数，非相同数量不能相乘
print(a4)
a5 = np.array([[1, 2], [4, 5]])
a6 = np.array([[7, 8], [10, 11]])
a7 = np.dot(a5, a6)  # 二维数组相乘，[[a,b],[c,d]] [[e,f],[g,h]]  结果[[ae+bg,af+bh],[ce+dg,cf+ch]]

a8 = np.array([[2, 3, 4], [5, 6, 7]])
a9 = np.arange(9).reshape(3, 3)
a10 = np.dot(a8, a9)  # 二维数组与三维数组相乘 乘数的第一行取出分别和被乘数的列相乘相加，每行乘以每列
X1 = np.array([[1, 2], [3, 4]])
X2 = np.array([[5, 6, 7], [8, 9, 10]])
X3 = np.dot(X1, X2)

# 数组与标量之间的运算，作用域数组中的每一个元素
n1 = np.arange(24).reshape((2, 3, 4))
n2 = n1.mean()  # 数组中所有元素的平均值
# print(np.abs(n1), np.fabs(n1), np.sqrt(n1), np.square(n1))  # 计算各元素的绝对值，绝对值，平方根，平方
# print(np.log(n1))

# 两个numpy数组的组合 | 添加行或者列

number = np.random.randint(1, 35, dtype=int, size=(5, 5))
number2 = np.random.randint(1, 13, dtype=int, size=(5, 2))
number3 = np.c_[number,number2]
number4 = np.r_[number3,number]