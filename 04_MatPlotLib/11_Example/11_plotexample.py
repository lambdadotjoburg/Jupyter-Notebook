# Import MatPlotLib Library and Assign a Name to it for Drawing Graphs

from matplotlib import pyplot as plt

# print(plt.style.available)

# Plot Style

plt.style.use('ggplot')

# Age (Horizontal Axis - Independent Variable)

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Median Salary for Developers (Vertical Axis - Dependent Variable 1)

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# Plot First Set of Points

plt.plot(ages_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Developers')

# Median Salary for Python Developers (Vertical Axis - Dependent Variable 2)

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

# Plot Second Set of Points

plt.plot(ages_x, py_dev_y, color='#5a7b9a', linestyle=':', marker='o', linewidth='2', label='Python')

# Median Salary for Javascript Developers (Vertical Axis - Dependent Variable 3)

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293]

# Plot Second Set of Points

plt.plot(ages_x, js_dev_y, color='#adad3b', linestyle='-.', marker='.', linewidth='2', label='JavaScript')

# Plot information

plt.xlabel('Ages')

plt.ylabel('Median Salary (USD)')

plt.title('Median Salary (USD) by Age')

# Assign Legends to Curves

plt.legend()

# Assign Grid to Graph Background

plt.grid(True)

# Padding/Margin

plt.tight_layout()

# Save Graph Programmatically

plt.savefig('C:/Users/Frank/Documents/Python/4_MatPlotLib/10_Example/Plot.svg')

# Make Plot

plt.show()