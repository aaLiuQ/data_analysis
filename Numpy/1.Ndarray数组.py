import numpy as np
import matplotlib.pyplot as plt

# 1.将列表转换成ndarray数组（一系列同类型数据的集合）
list1 = [1, 5, 6, 11, 0.1, '45']
np1 = np.array(list1)

# 2.嵌套列表可以转换成多维ndarray
list2 = [[1, 2, 0.5], [6, 8, 7]]
np2 = np.array(list2)

# 2.1 ndarray数组的属性
a1 = np.random.rand(21).reshape(3, 7)
# print(a1.ndim, a1.shape, a1.size, a1.dtype, a1.itemsize)  # 数组的维度，形状，数量，类型，每个元素的大小（字节单位）

# 2.2 使用使用列表或元组创建数组时，如果不指定类型，会自动关联一个dtype类型
# a2 = np.array([[1, 2, 6], [-1, -2, 0.2], (1, 2)])
# print(a2.dtype) object  # ndarray数组.dtype方法可以获得数组的类型
a3 = np.arange(10)  # 返回一个0-9的ndarray数组

# 3.利用random生成随机数组
nd3 = np.random.random([4, 3])  # 生成4行3列0-1的随机数组,数组对象.shape方法可以打印出数组的形状
np.random.seed(123)  # 用来使每一次生成的随机数都是同一份
np4 = np.random.randn(2, 4, 3)  # 生成0-1的两层 4*3的多维数组
np.random.shuffle(np4)  # 用于打乱生成的数组，但其实还是同一份
np19 = np.random.randint(1, 20, (2, 3))  # 指定范围内生成随机数，按照指定的形状生成
np20 = np.random.normal(0, 1, (10, 5))  # 生成高斯分布的概率密度随机数
# choice(a, size, replace, p)：从一维数组a中以概率p抽取元素，形成size形状的新数组，replace表示是否可以重用元素，默认为True


# 4.创建特定形状的多维数组
np5 = np.zeros([3, 3], dtype=np.int32)  # 生成全是0的3*3数组
np6 = np.ones([3, 3])  # 生成全是1的3*3数组
np7 = np.eye(4)  # 生成4*4的数组，对角线为1
np8 = np.diag([1, 4, 5, 6])  # 生成4阶的对角数组，对角线是列表内容
np13 = np.full((3, 4), 2)  # 生成一个3*4的数组，内容是指定的内容
np14 = np.ones_like(np13)  # 生成一个形状和数组相同但内容为1的数组，no.zeros_like使用方法相同
np15 = np.full_like(np14, 4, dtype=int)  # 根据数组形状形成一个内容为指定的数组

# 5.数组快速存储文件和读取
s1 = np.arange(24).reshape((3, 8))
np.savetxt('a.csv', X=s1, fmt='%d', delimiter=',')  # 一维和二维数组的存储，保存的文件名称，存储的对象，存入文件的格式，分隔符
d = np.loadtxt('a.csv', delimiter=',', dtype=int)

# 5.2 多维数组的存储和读取
s2 = np.arange(24).reshape((2, 3, 4))
# a.tofile(frame, sep='', format='%s')  多维数组的存储
# np.fromfile(frame, dtype=np.float, count=-1, sep='')  多维数组的读取

# 6.利用arange() 和linspace()函数生成数组
np11 = np.arange(10, 0, -1)  # 用法和range相同，始，终，步长，步长可以是小数和负数
np12 = np.linspace(1, 20, 20, retstep=True, endpoint=False, dtype=object)  # start:开始，stop:结束，num:默认是50个样本点，
# restep:步长，第一个数据和第二个数据的距离，endpoint：默认是True，改为false则取不到右端点，dtype:可以设置数值类型

# 7.np.concatenate组合数组
np17 = np.arange(1, 20, 3)
np18 = np.linspace(1, 20, 4)
np16 = np.concatenate((np17, np18))

# print(np16)
