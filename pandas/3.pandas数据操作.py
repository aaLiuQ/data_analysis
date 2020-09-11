# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

s5 = np.random.normal(0, 1, (10, 5))

s6 = pd.DataFrame(s5)

s7 = ['数据' + str(i) for i in range(s6.shape[0])]
s8 = pd.DataFrame(s5, index=s7)
s9 = pd.date_range('2017-01-01', periods=s6.shape[1], freq='B')
s10 = pd.DataFrame(s5, index=s7, columns=s9)


# 1.DataFrame索引操作
# 1.1 直接使用行列索引
# print(s10)
# print(s10['2017-01-06']['数据0'])

# 1.2结合loc使用行列索引下标截取
# print(s10.loc['数据0':'数据5', '2017-01-02'])
# 1.3结合iloc使用索引下标
# print(s10.iloc[0:3, 0:2].head())

# 1.3 使用ix组合索引下标  现版本已移除ix方法，推荐使用loc 和 iloc
# print(s10)
# print(s10.loc[s10.index[0:4]])
# print(s10.loc[['数据0', '数据1', '数据2', '数据3']])
# print(s10.iloc[0:4], s10.columns.get_indexer(['数据0', '数据1', '数据2', '数据3']))  # 列索引 获取行索引

# 1.4 DataFrame赋值操作
# 可以直接修改原来的值,修改整个列整个行的值
# s10['2017-01-02'] = '2016-12-31'
# s10['数据0'] = '111'

# 1.5 排序
# 1.5.1 使用df.sort_values(by=,ascend=) 单个键或者多个键进行排序，ascend=False 降序 True 升序
s11 = s10.sort_values(by='2017-01-02', ascending=False).head()
s12 = s10.sort_values(by=['2017-01-02', '2017-01-03'])  # 按照多个键排序
# 1.5.2 使用df.sort_index() # 进行索引排序，貌似会放弃掉原先的索引
s13 = s10.set_index('2017-01-02')
print(dir())
