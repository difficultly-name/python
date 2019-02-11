import numpy as np
import pandas as pd
num_list = []


def num():
    num = np.random.randint(1, 101)
    num_list.append(num)


for i in range(1, 10000):
    num()
s = pd.Series(num_list)
print(s.describe())
print(num_list)








