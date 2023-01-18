import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, CheckButtons
 
 
fig = plt.figure()
ax = fig.subplots()
plt.subplots_adjust(left=0.3, bottom=0.25)
 
x1 = np.array([0, 1, 2, 3])
y1 = np.array([5, 2, 8, 6])
p, = ax.plot(x1, y1, color="blue", marker="o")
 
x2 = np.array([0, 1, 2, 3])
y2 = np.array([10, 2, 0, 12])
p1, = ax.plot(x2, y2, color="green", marker="o")
 
x3 = np.array([0, 1, 2, 3])
y3 = np.array([0, 3, 2, 19])
p2, = ax.plot(x3, y3, color="yellow", marker="o")
lines = [p, p1, p2]
labels = ["plot1", "plot2", "plot3"]
 
 
def func(label):
    index = labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    fig.canvas.draw()
 
 
label = [True, True, True]
 
# xposition, yposition, width and height
ax_check = plt.axes([0.9, 0.001, 0.2, 0.3])
plot_button = CheckButtons(ax_check, labels, label)
plot_button.on_clicked(func)
 
plt.show()