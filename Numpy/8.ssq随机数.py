import numpy as np

number = np.random.randint(1, 35, dtype=int, size=(5, 5))
number2 = np.random.randint(1, 13, dtype=int, size=(5, 2))
number3 = np.c_[number, number2]

for nums in number3:
    print(nums)

"""
[34  7  2 17  4 11  8]
[ 7 17 33 29 18  7 11]
[34  5 11 29 24 11 12]
[ 8  8 30  3 14  1  1]
[ 9  8 33 21 34  2  5]

02 04 07 17 34  08 11
03 09 18 29 33  03 07
05 11 14 24 31  11 12
01 02 08 14 23  01 10
05 09 13 21 35  02 05 

"""
