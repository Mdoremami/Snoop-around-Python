import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np
import os
from pandas import read_csv
path = 'E:\\My Projects\\2019 Works\\Python\\Sublime\\Matplotlib'
os.chdir('E:\\My World\\EDUCATION\\Main\\My Pythonism\\Matplotlib Tutorials')
print(os.getcwd())

# Histograms
data = read_csv('data.csv' , delimiter = ';')
os.chdir(path)
print(data)

Ages = data['Age']
Dev_Sals = data['All_Devs']
Py_Sals = data['Python']
Js_Sals = data['JavaScript']


plt.style.use('ggplot')
# A fairly bad figure...
plt.hist(Ages)
plt.show()
# Let's make it right
bins = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 , 100]
plt.hist(Ages , bins = bins)
plt.show()
# Better, but still needs to get better. If values were so large, for example 10^3 people were in their 30s, we can
# set 'log = True' option to show it as 10^3 in y-axis.
plt.hist(Ages , bins = bins , edgecolor = 'w' , color = 'b')
# We can also set a median line
plt.axvline(26 , color = 'r' , label = 'median age')
plt.legend()
plt.show()
