import numpy as np

number = np.random.randint(1, 35, dtype=int, size=(5, 5))
number2 = np.random.randint(1, 13, dtype=int, size=(5, 2))
number3 = np.c_[number, number2]

for nums in number3:
    print(nums)
