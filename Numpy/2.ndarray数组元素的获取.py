import numpy as np

#  1.ndarray数组元素的截取和list，tuple类似,始，终，步长
# np.random.seed(2020)
np1 = np.random.random([10])
# print(np1)
# print(np1[3], np1[3:6], np1[1:6:2], np1[::-2])

#  2.多维数组的截取也支持步长，多个[]内是取指定行列，单个[x:y:z,x:y:z]是取x到y行步长为z, 取x到y列步长为z，左开右关

np2 = np.arange(25).reshape([5, 5])  # 创建5*5 的多维数组,
np3 = np2[1:3, 1:3]  # 多维数组的截取，左关右开，[2:5, 2:5]截取的数组是：3*3 - 5*5
np4 = np2[(np2 >= 3) & (np2 < 10)]  # 纯粹的取区间
np5 = np2[[0, 3]]  # 取指定的行 第一行和第四行
np6 = np2[:, 1:3]  # 取指定的列 第二列和第三列 左开右关，最右边可以用于取行
np7 = np2[2::2, ::2]  # 第三行开始取行，步长为二，从第一列开始取列，步长为2
np8 = np.arange(24).reshape(2, 3, 4)
np9 = np8[1, 2, 3]  # 普通的多维数组截取：维度为2 的第三行第四列
np10 = np8[:, 1:3, :]  # 行和列都取第二行和第三行
print(np8)
print(np10)

# 3.通过函数取值
a = np.arange(1, 25, dtype=float)
a2 = np.random.choice(a, size=(2, 3), replace=True)  # 通过.chioce方法随机抽值，size指定形状，replace为True则代表可以重复取值
a3 = np.sum(a)
a4 = a / np.sum(a)
a5 = np.random.choice(a, size=(3, 8), p=a / np.sum(a))  # np.sum(a)计算a的总和，p = a中的每个数除以总和，则算成他的概率
