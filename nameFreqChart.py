import numpy as numpy
import pandas as pd

import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

df = pd.read_csv("frequency.csv")
sum_column = df.sum(axis=0, numeric_only=True)

names, nums = [], []
for i, val in sum_column.items():
	#print(i, val)
	if val >= 0:
		names.append(i)
		nums.append(val)

zipped_lists = zip(nums, names)
sorted_pairs = sorted(zipped_lists)

tuples = zip(*sorted_pairs)
nums, names = [ list(tupl) for tupl in  tuples]

plt.bar(names, nums, color='blue')
plt.xlabel("Individuals")
plt.xticks(rotation = 45, fontsize=4,)
plt.ylabel("Mentions")
plt.title("All Individuals")

plt.show()