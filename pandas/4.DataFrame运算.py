# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

s5 = np.random.normal(0, 1, (10, 5))
s6 = pd.DataFrame(s5)
s7 = ['数据' + str(i) for i in range(s6.shape[0])]
s8 = pd.DataFrame(s5, index=s7)
s9 = pd.date_range('2017-01-01', periods=s6.shape[1], freq='B')
data = pd.DataFrame(s5, index=s7, columns=s9)

# 1.算数元素
# 1.1 add() 直接加上一个具体的值,该索引 行/列 所有数据直接进行加算
data1 = data['2017-01-02'].add(10)

# 1.2 sub() 应该是直接做减法运算,取出两列的值进行相关加减在赋给另一列
date1 = data['2017-01-02']
date2 = data['2017-01-03']
data['2017-01-07'] = date1.sub(date2)
print(data)


