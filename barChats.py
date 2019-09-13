import matplotlib.pyplot as plt
import numpy as np
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_indexes = np.arange(len(ages_x))
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

#notice the change
width = 0.25   
plt.bar(x_indexes-width,py_dev_y,width=width)
plt.bar(x_indexes,dev_y,width=width)


plt.xlabel('ages')   #x-axis label
plt.ylabel('Median Salary') #y-axis label
plt.title("median salary (USD) by age") # title of the graph
plt.xticks(x_indexes,ages_x)
plt.show()