import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np
import os
from pandas import read_csv
path = 'E:\\My Projects\\2019 Works\\Python\\Sublime\\Matplotlib'
os.chdir('E:\\My World\\EDUCATION\\Main\\My Pythonism\\Matplotlib Tutorials')
print(os.getcwd())

# Professional Linear Plots
data = read_csv('data.csv' , delimiter = ';')
os.chdir(path)
print(data)

Ages = data['Age']
Dev_Sals = data['All_Devs']
Py_Sals = data['Python']
Js_Sals = data['JavaScript']

# plt.figure(figsize = (8,5))
plt.style.use('ggplot')
plt.plot(Ages , Dev_Sals , color = 'k' , linestyle = '-' , label = 'All Developers')
plt.plot(Ages , Py_Sals , color = 'g' , linestyle = '--' , label = 'Python Developers')

# We can fill within a line on the chart:
# alpha is the saturation parameter
# y2 parameter is the center point of oscillation I'd like to call...
# Mainly, it devides the parts beneath a specific number and above it (Median). It will actually bend the graph over that center point
# Where, sets a condition to fill beneath the line plotted
Average_Sal = 50000
plt.fill_between(Ages , Dev_Sals , alpha = 0.8 , y2=Average_Sal , where = Dev_Sals > Average_Sal , color = 'b' , interpolate = True)

# We can also do have colorings for the graph below the median and above it.
plt.fill_between(Ages , Dev_Sals , alpha = 0.8 , y2=Average_Sal , where = Dev_Sals <= Average_Sal , color = 'r' , interpolate = True)
# if you pay attention, you would have small parts around the center point uncolored. It can be solved by setting interpolate=True


plt.legend()
plt.title('Developers'' Salaries')
plt.xlabel('Ages')
plt.ylabel('Salaries')
plt.savefig('bb.png')
# Fixes the axis labels appearence and you don't have to manually do figsize in plt.figure
plt.tight_layout()
plt.show()
# # Want to automatically close plots? use 'False' for 'block' value in 'plt.show()' and use 'plt.pause(secs)' afterwards
# plt.show(False)
# plt.pause(5)
# plt.close()

