# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

# pandas包括两种数据类型，series和dataframe.
# series是一种一维数据结构，每个元素都带有一个索引，索引可以为数字或者字符串，结构：索引列|数据列
# dataframe数据帧：是一种二维数据结构，数据以表格形式存储，有对应的行和列 结构：索引列|列名|数据列

# series series结构只有行索引
# 1.从列表 元组 字典构建series
list1 = list('abcdefghijklmnopqrstuvwxyz')
tuple1 = np.arange(26)
dict1 = dict(zip(list1, tuple1))
ser1 = pd.Series(list1)
ser2 = pd.Series(tuple1)
ser3 = pd.Series(dict1)
# 1.1创建series并指定索引
ser5 = pd.Series([1, 2, 3, 4], index=[5, 6, 7, 8])
print(ser5)
print(ser5.index, ser5.values)

# 2.将series转换成dataframe
df = ser3.to_frame()
# 索引列转换成dataframe的列
df.reset_index(inplace=True)

# 将多个series组合成dataframe
# 方法1 axis=1表示列拼接，=0表示行拼接
df = pd.concat([ser1, ser2], axis=1)
# 方法2，用字典的方式设置列名
df2 = pd.DataFrame({'col1': ser1, 'col2': ser2})

# series命名列索引的名称
ser4 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser4.name = '刘强'

# 两个series对象的比较
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
# 返回ser1不包含ser2的布尔型series
ser3 = ~ser1.isin(ser2)
# print(ser3)
# 返回两个series对交集和并集


# 2.DataFrame数据帧
s5 = np.random.normal(0, 1, (10, 5))
s6 = pd.DataFrame(s5)

# 构造行索引数据
s7 = ['股票' + str(i) for i in range(s6.shape[0])]
# 添加行索引，index用于添加一个列表，列表的索引数等于行数，0轴，axis=0
s8 = pd.DataFrame(s5, index=s7)

# 添加列索引
# pd.date_range()：用于生成一组连续的时间序列
# date_range(start=None,end=None, periods=None, freq='B') 开始时间 结束时间 时间天数 递进单位‘B’默认掠过周末
# 使用data_range构造列索引
s9 = pd.date_range('2017-01-01', periods=s6.shape[1], freq='B')
# 添加列索引,在DataFrame方法里面添加columns参数 1轴 axis=1
s10 = pd.DataFrame(s5, index=s7, columns=s9)

# print(s10.shape, s10.index, s10.columns, s10.values)  # dataframe参数的形状，行索引，列索引,值
s11 = s10.T  # 转置，行和列的转换

# 2.1 DatatFrame索引的设置
# 在修改时，不能单一只修改一个，需要修改整体
# reset_index(drop=False)重设索引，drop默认为false,如果为True,删除原来的索引
s12 = s10.reset_index(drop=True)
# print(s12)
# 2.2 以某列值设置为新的索引 set_index(keys,drop=true) 列索引名或者索引名称的列表 删除原来列
d1 = pd.DataFrame({
    'month': [1, 4, 7, 10],
    'year': [2012, 2014, 2013, 2014],
    'sale': [55, 40, 83, 31]
})
d2 = d1.set_index('month')
# 设置多个索引
d3 = d1.set_index(['year', 'month'])

# 2.2 MultiIndex多级或分层索引对象
# index属性：name:levels名称，level;每个level的元组值
d4 = d3.index.names
d5 = d3.index.levels

# 3.Panel 用于存储三维数组的panel结构  Pandas从版本0.20.0开始弃用：推荐的用于表示3D数据的方法是通过DataFrame上的MultiIndex
# p = pd.Panel(np.arange(24).reshape(4, 3, 2),
#              items=list('ABCD'),
#              major_axis=pd.date_range('20130101', periods=3),
#              minor_axis=['first', 'second'])

# 4.多重索引multIndex  # 后续补充
m1 = pd.DataFrame({'class': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C'],
                   'id': ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b'],
                   'value': [1, 2, 3, 4, 5, 6, 7, 8]})
m1.set_index(['class', 'id'], inplace=True)
# print(m1.loc['A', :])

# 5.
