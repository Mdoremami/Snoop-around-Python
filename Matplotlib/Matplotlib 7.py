import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np
import os
from pandas import read_csv
path = 'E:\\My Projects\\2019 Works\\Python\\Sublime\\Matplotlib'
os.chdir('E:\\My World\\EDUCATION\\Main\\My Pythonism\\Matplotlib Tutorials')
print(os.getcwd())

# Scatter Plots
data = read_csv('data.csv' , delimiter = ';')
os.chdir(path)
print(data)

Ages = data['Age']
Dev_Sals = data['All_Devs']
Py_Sals = data['Python']
Js_Sals = data['JavaScript']


plt.style.use('ggplot')
# s=size of the scatter poings, c is color (c='magenta'), edgecolor is clear, linewidths is for the width of the edge lines, alpha for
# transparecy , marker for the shape of the scatter points
# for color, you can write the name of the color or just create a list of numbers as large as your data.
# cmap is the color map that can be set to : Reds, Greens, Blues, summer,spring,winter,autumn, etc.
# It'll give a spectrum of colors in that color area. I have to mention that with different colors, cmap could be really
# showing itself.
# we also can set different sizes as well...
sizes = np.linspace(50,300,38) # For different sizes
colors = np.sort(np.random.randint(1,1000,38)) # For different colors
plt.scatter(Ages , Py_Sals , s=sizes  , c=colors, cmap = 'winter' , linewidths = 0.5 , edgecolor = 'k' , marker = 'X' , alpha = 0.6)
# We can use a colorbar to determine what are the colors for
cbar = plt.colorbar()
cbar.set_label('Satisfaction')
plt.show()
