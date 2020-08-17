import matplotlib.pyplot as plt
import numpy as np
import os
from itertools import count
from matplotlib.animation import FuncAnimation
from pandas import read_csv
path = 'E:\\My Projects\\2019 Works\\Python\\Sublime\\Matplotlib'
os.chdir(path)


# # Live Charts
# # First, a little about count module
# x = count()
# for i in range(20):
# 	print(next(x))

# # Now, we need a function to create the animation
# x_vals = []
# y_vals = []
# index = count()
# def animator(i):
# 	x_vals.append(next(index))
# 	y_vals.append(np.random.randint(0,5,1))
# 	# plt.cla() clears the previous axis. Without it, it's like that plt is plotting the lines on each other.
# 	# You can do plt.cla() to clear axis or plt.clf() to clear the figure
# 	plt.cla()
# 	plt.plot(x_vals , y_vals)
# # We need to pass 'figure' and 'function' and the 'interval' is the time for updating the plot in miliseconds
# anime = FuncAnimation(plt.gcf() , animator , interval = 300)
# plt.tight_layout()
# plt.show()


# Now, we will be doing an awesome job...
# We want to create a CSV file and fill it with random
# numbers. So, we'll do it by our function.
# Then, we will see the live animation as well.
# We need a second kernel to run this, so you can use
# ipython for example.. in cmd
os.chdir('CSVDataGenerator')
index = count()

def animator(i):
	data = read_csv('data.csv')
	x_vals = data['xvals']
	y1 = data['total_1']
	y2 = data['total_2']
	# plt.cla() clears the previous axis. Without it, it's like that plt is plotting the lines on each other.
	# You can do plt.cla() to clear axis or plt.clf() to clear the figure
	plt.cla()
	plt.plot(x_vals , y1 , label = 'channel 1')
	plt.plot(x_vals , y2 , label = 'channel 2')
	plt.legend()
	plt.tight_layout()

anime = FuncAnimation(plt.gcf() ,
		animator , interval = 300)

plt.tight_layout()
plt.show()


