# -*- coding: UTF-8 -*-
import numpy as np

# 处理大量数据的方法：得到数据集-->随机打乱数据-->定义批量大小-->批量处理数据集

datas = np.random.rand(2000,2,3)
# 随机打乱数据
np.random.shuffle(datas)
# 定义批量大小
size = 100
# 进行批量处理
for i in range(0,len(datas),size):
    size_sum = np.sum(datas[i:i+size])
    print("第{}批次，该批次数据之和为{}".format(i,size_sum))
