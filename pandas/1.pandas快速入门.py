# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

# 1.对象创建
s1 = pd.Series([1, 3, 5, np.nan, 6, 8])  # 利用传递值来创建一个列表
s2 = pd.date_range('20170101', periods=7)
s3 = pd.DataFrame(np.random.rand(7, 4), index=s2, columns=list('1234'))  # 通过传递numpy数组，使用datetime索引和标记列来创建DataFrame：
# print(s3.tail())  # 数据帧对象.head()方法用于显示头部5个，tail()用于显示尾部5个

# 通过传递可以转换为类似系列的对象的字典来创建DataFrame
s4 = pd.DataFrame({'A': 1.,
                   'B': pd.Timestamp('20170102'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([3] * 4, dtype='int32'),
                   'E': pd.Categorical(["test", "train", "test", "train"]),
                   'F': 'foo'})

print(pd.__version__)
