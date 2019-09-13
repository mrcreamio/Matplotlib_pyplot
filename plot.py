import matplotlib.pyplot as plt
import numpy as np
plt.style.use("fivethirtyeight")
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_indexes = np.arange(len(ages_x))
width = 0.25
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(x_indexes - width,dev_y,width=width,label='All devs')
plt.xlabel('ages')
plt.ylabel('Median Salary')
plt.title("median salary (USD) by age")
# plt.show()
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.bar(x_indexes,py_dev_y,width=width,label='Python')
plt.xticks(x_indexes,ages_x)
plt.xlabel('ages')
plt.ylabel('Median Salary')
plt.title("median salary (USD) by age")

plt.tight_layout()
plt.legend()
plt.show()